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


# Load User info
def load_user(con, username):
    user_accounts = []
    if con.is_connected:
        user_accounts = load_accounts(con, username)

        if not len(user_accounts) > 0:
            print('No accounts created')
            return user_accounts
        else:
            return user_accounts
