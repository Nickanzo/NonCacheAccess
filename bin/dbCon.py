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
import mysql.connector  # DB Connection
import settings  # Global Data
from mysql.connector import DatabaseError  # SQL Error Handler
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


def verify_login(con, user, password):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT COUNT(*) FROM login WHERE username = %s AND password = %s'  # Create SQL statement
            values = (user, password)  # Use params for statement values
            cursor.execute(sql, values)
            (rows,) = cursor.fetchone()
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


# ---------------------------------------------------------------------------
# Account Management methods
# ---------------------------------------------------------------------------
# Load all the accounts the user logged has
def load_accounts(con, user):
    account = []  # List for number of accounts
    web_accounts = []  # List for number of websites
    domain = ''
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT accountName, accountURL FROM accounts WHERE username = %s'  # Create SQL statement
            values = (user,)  # Use params for statement values
            cursor.execute(sql, values)
            for accountName, accountURL in enumerate(cursor):  # Retrieve found values
                if domain == accountURL:  # Check last URL
                    account.append(accountName)  # Append
                else:
                    web_accounts.append(accountURL)  # Append a new URL
                    account.append(accountName)  # Append
                domain = accountURL
        except mysql.connector.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()
        web_accounts.append(account)
        return web_accounts


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
