#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Database related tests """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from bin.dbCon import create_account, delete_account, load_accounts  # DB connection
from bin.login import login
import settings  # App Global info

if __name__ == '__main__':

    # |✓| 1st Test, Log In
    logged = login('p3pito', 'pepo123')
    print(logged.is_connected())

    # |✓| 2nd Test, Create Accounts
    if login:
        print(create_account(logged, settings.__user__, 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))
        print(create_account(logged, settings.__user__, 'pepo2@email.com', 'pepo1234', 'EmailPepito2', 'www.gmail.com'))
        print(create_account(logged, settings.__user__, 'pepo3@email.com', 'pepo1235', 'EmailPepito3', 'www.gmail.com'))
        print(create_account(logged, settings.__user__, 'pepo4@email.com', 'pepo1236', 'EmailPepito4', 'www.gmail.com'))
        print(create_account(logged, settings.__user__, 'pepo5@email.com', 'pepo1237', 'EmailPepito5', 'www.gmail.com'))
        print(create_account(logged, settings.__user__, 'pepo@domain.com', 'pepodom', 'DomPepito', 'www.pepito.com'))

    # |✓| 3rd Test, Don't allow create Account for different Login
        print(create_account(logged, 'pepita', 'pepa@email.com', 'pepa123', 'EmailPepita', 'www.gmail.com'))
        print(create_account(logged, 'pepito', 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))

    # |✓| 4th Test, Don't allow create same Account twice
        print(create_account(logged, settings.__user__, 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))

    # |✓| 5th Test, Delete Accounts
        print(delete_account(logged, settings.__user__, 'pepo@email.com', 'www.gmail.com'))

    # |✓| 6th Test, Only Delete Existing Accounts
        print(delete_account(logged, 'pepita', 'pepa@email.com', 'www.gmail.com'))

    # |✓| 7th Test, Load Accounts
        print(load_accounts(logged, settings.__user__))
