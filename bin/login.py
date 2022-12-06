#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Login screen """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from bin.dbCon import create_con, verify_login
import settings  # App Global Data


# Login method for account management display
def login(username, password):
    settings.init()
    # Create DB connection using settings.py definitions
    con = create_con(settings.HOST, settings.USER, settings.PASSWORD, settings.NAME)

    #Verify if the connection succeeded
    if not con.is_connected():
        print("DB connection error!")
    else:
        settings.__con__ = con
        #Search username/password in the DB
        if verify_login(con, username, password):
            settings.__user__ = username
            return con
        else:
            con.close()
            return con
