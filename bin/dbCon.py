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
from mysql.connector import DatabaseError  # SQL Error Handler
from urllib.parse import urlparse  # URL handler


# ---------------------------------------------------------------------------
# Database Connection
# ---------------------------------------------------------------------------
# Create and return DB connection using params
def create_con(host, user, password, db):
    return mysql.connector.connect(host=host, user=user, password=password, database=db)


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
            except mysql.Error as e:
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
            except mysql.Error as e:
                msg = 'Failed to delete user {0}. Error: {1}'.format(sql, e)  # Show error message
                raise DatabaseError(msg)
            finally:  # Terminate Cursor
                cursor.close()

            print('User deleted!')  # Success message

            con.commit()  # Commit changes to the DB


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
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'SELECT accountName, accountURL FROM accounts WHERE username = %s'  # Create SQL statement
            values = user  # Use params for statement values
            cursor.execute(sql, values)
            for accountName, accountURL in cursor:  # Retrieve found values
                if not domain == urlparse(accountURL).netloc:  # Check last URL
                    account.append(accountName)  # Append a new Account name
                else:
                    web_accounts.append(urlparse(accountURL).netloc)  # Append a new URL
                    web_accounts.append(account)  # Append list of account names
                domain = urlparse(accountURL).netloc
        except mysql.Error as e:
            msg = 'Failed to execute SQL statement {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()

        return web_accounts


# Create a new account for the user logged
def create_account(con, username, accountLogin, accountPassword, accountName, accountURL):
    if con.is_connected:
        cursor = con.cursor()  # Get Cursor
        try:
            sql = 'INSERT INTO accounts ( username, accountLogin, accountPassword,' \
                  ' accountName, accountURL ) values (%s,%s,%s,%s,%s)'  # Create SQL statement
            values = (username, accountLogin, accountPassword, accountName, accountURL)  # Use params for statement
            cursor.execute(sql, values)
        except mysql.Error as e:
            msg = 'Failed to insert account {0}. Error: {1}'.format(sql, e)  # Show error message
            raise DatabaseError(msg)
        finally:
            cursor.close()
        con.commit()  # Commit changes to the DB
        print('Account created!')
