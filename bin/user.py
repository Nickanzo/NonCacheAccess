#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" User account management processes and methods """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from settings import *
from getpass import getpass, getuser
from dbCon import load_accounts, create_account

global __user__


# Load User info
def load_user(con, username):
    user_accounts = []
    if con.is_connected:
        __user__ = username
        user_accounts = load_accounts(con, username)

        if not len(user_accounts) > 0:
            answer = input('User has no accounts, do you want to create one? [Y/N]')
            if not answer == 'N':
                accountLogin = getuser('Login: ')
                accountPassword = getpass('Password: ')
                accountName = input('Account nickname: ')
                accountURL = input('URL: ')
                create_account(con, username, accountLogin, accountPassword, accountName, accountURL)
        else:
            for accounts in user_accounts:
                print(accounts)
