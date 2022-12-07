#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Database related processes and methods """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import os

import mysql.connector  # DB Connection
import settings  # Global Data
from mysql.connector import DatabaseError  # SQL Error Handler
import hashlib
import base64
import bcrypt
from urllib.parse import urlparse  # URL handler


# ---------------------------------------------------------------------------
# Database Connection
# ---------------------------------------------------------------------------
# Create and return DB connection using params
def create_con(host, user, password, db):
    try:
        return mysql.connector.connect(host=host, user=user, password=password, database=db)
    except mysql.connector.Error as e:
        msg = 'Failed DB connection {0}. Error: {1}'  # Show error message
        raise DatabaseError(msg)


# Close DB Connection
def close_con(con):
    return con.close()


def retrieve_con():
    try:
        return mysql.connector.connect(host=settings.HOST, user=settings.USER,
                                       password=settings.PASSWORD, database=settings.NAME)
    except mysql.connector.Error as e:
        msg = 'Failed DB connection {0}. Error: {1}'  # Show error message
        raise DatabaseError(msg)


# ---------------------------------------------------------------------------
# Login methods
# ---------------------------------------------------------------------------
# Create Login user
def create_user(con, user, password):
    if not con.is_connected():  # Verify DB connection
        print('DB connection error')
    else:
        if bool(verify_user(con, user)):  # Search if user exists
            print('User already exists!')
        else:
            cursor = con.cursor()  # Get Cursor
            try:
                sql = 'INSERT INTO login (username, password) values (%s, %s)'  # Create SQL statement
                values = (user, password)  # Use params for statement values
                cursor.execute(sql, values)  # Execute SQL statement
            except mysql.connector.Error as e:
                msg = 'Failed to insert user {0}. Error: {1}'.format(sql, e)  # Show error message
                raise DatabaseError(msg)
            finally:  # Terminate Cursor
                cursor.close()

            print('User created!')  # Success message

            con.commit()  # Commit changes to the DB

            return True


# Delete Login user
def delete_user(con, user):
    if not con.is_connected():  # Verify DB connection
        print('DB connection error')
    else:
        if not bool(verify_user(con, user)):  # Search if user exists
            print('User not found!')
        else:
            cursor = con.cursor()  # Get Cursor
            try:
                sql = 'DELETE FROM login WHERE username = %s'  # Create SQL statement
                values = (user,)  # Use params for statement values
                cursor.execute(sql, values)  # Execute SQL statement
            except mysql.connector.Error as e:
                msg = 'Failed to delete user {0}. Error: {1}'.format(sql, e)  # Show error message
                raise DatabaseError(msg)
            finally:  # Terminate Cursor
                cursor.close()

            print('User deleted!')  # Success message

            con.commit()  # Commit changes to the DB


def verify_login(con, user, pwd):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT username, password FROM login WHERE username = %s'  # Create SQL statement
            values = (user,)  # Use params for statement values
            cursor.execute(sql, values)
            for username, password in cursor:
                if bcrypt.checkpw(pwd.encode("utf-8"), password.encode('utf-8')) and username == user:
                    return True
                else:
                    return False
            #(rows,) = cursor.fetchone()
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()

        return bool(rows)


# Verify user in DB
def verify_user(con, user):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT COUNT(*) FROM login WHERE username = %s'  # Create SQL statement
            values = (user,)  # Use params for statement values
            cursor.execute(sql, values)
            (rows,) = cursor.fetchone()
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()

        return bool(rows)


def createKey(key):

    encrypted = hashlib.md5(key.encode())

    return encrypted.hexdigest().upper()


def encryptPass(key):

    hash = bcrypt.hashpw(key.encode("utf-8"), bcrypt.gensalt())

    return hash


def customEncrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def customDecrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)


# ---------------------------------------------------------------------------
# Account Management methods
# ---------------------------------------------------------------------------
# Load all the accounts the user logged has
def load_accounts(con, user):
    web_accounts = []  # List for number of websites
    domain = ''
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT accountName, accountURL FROM accounts WHERE username = %s'  # Create SQL statement
            values = (user,)  # Use params for statement values
            cursor.execute(sql, values)
            for accountName, accountURL in cursor:  # Retrieve found values
                if domain == accountURL:  # Check last URL
                    web_accounts.append(accountName)  # Append
                else:
                    web_accounts.append(accountURL)  # Append a new URL
                    web_accounts.append(accountName)  # Append
                domain = accountURL
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()
        return web_accounts


def retrieve_account(con, accountName):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT accountLogin, accountPassword, accountURL FROM accounts WHERE accountName = %s'  # Create SQL statement
            values = (accountName,)  # Use params for statement values
            cursor.execute(sql, values)
            result = cursor.fetchone()

            sql = 'SELECT URL, name FROM websites WHERE name = %s'  # Create SQL statement
            values = (result[2],)
            cursor.execute(sql, values)
            result_aux = cursor.fetchone()
            account = list()
            account.append(result[0])
            account.append(result[1])
            account.append(result_aux[0])
            account.append(result_aux[1])

            return account
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()


def load_websites(con):
    if con.is_connected:
        cursor = con.cursor()
        try:
            sql = 'SELECT name FROM websites'
            cursor.execute(sql)
            websites = [r for r, in cursor]
            #websites = cursor.fetchall()
            #websites = list(cursor.fetchall())
            return websites
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()


# Create a new account for the user logged
def create_account(con, username, accountLogin, accountPassword, accountName, accountURL):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        if not username == settings.__user__:
            print('Account creation only permitted for Logged User, please log in and try again')
            return False
        elif verify_account(con, settings.__user__, accountLogin, accountURL):
            print('The account was created already!')
            return False
        else:
            try:
                sql = 'INSERT INTO accounts ( username, accountLogin, accountPassword,' \
                      ' accountName, accountURL ) values (%s,%s,%s,%s,%s)'  # Create SQL statement
                values = (username, accountLogin, accountPassword, accountName, accountURL)  # Use params for statement
                cursor.execute(sql, values)
            except mysql.connector.Error as e:
                msg = 'Failed to insert account {0}. Error: {1}'.format(sql, e)  # Show error message
                raise DatabaseError(msg)
            finally:
                cursor.close()
            con.commit()  # Commit changes to the DB
            print('Account created!')
            return True


# Delete account for the Logged user
def delete_account(con, username, accountLogin, accountURL):
    if con.is_connected:
        if not verify_account(con, username, accountLogin, accountURL):
            print('Account doesn´t exist')
            return False
        else:
            cursor = con.cursor()  # Get Cursor
            try:
                # Create SQL statement
                sql = 'DELETE FROM accounts WHERE username = %s AND accountLogin = %s AND accountURL = %s'
                values = (username, accountLogin, accountURL)  # Use params for statement values
                cursor.execute(sql, values)  # Execute SQL statement
            except mysql.connector.Error as e:
                msg = 'Failed to delete user {0}. Error: {1}'.format(sql, e)  # Show error message
                raise DatabaseError(msg)
            finally:  # Terminate Cursor
                cursor.close()
            con.commit()  # Commit changes to the DB
            print('Account deleted!')  # Success message
            return True


# Verify if the account already exists
def verify_account(con, username, accountLogin, accountURL):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            # Create SQL statement
            sql = 'SELECT COUNT(*) FROM accounts WHERE username = %s AND accountLogin = %s AND accountURL = %s'
            values = (username, accountLogin, accountURL)  # Use params for statement values
            cursor.execute(sql, values)
            (rows,) = cursor.fetchone()
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()

        return bool(rows)
