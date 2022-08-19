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
from dbCon import create_con, verify_user
from settings import *


# Login method for account management display
def login(username, password):
    # Create DB connection using settings.py definitions
    con = create_con(HOST, USER, PASSWORD, NAME)

    #Verify if the connection succeeded
    if not con.is_connected():
        print("DB connection error!")
    else:
        #Search the username/password in the DB
        if verify_user(con, username):
            print("Success!")
        else:
            print("Username or Password incorrect!")
