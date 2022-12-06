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
import unittest
from bin.dbCon import *  # DB connection
from settings import *  # App Global info



if __name__ == '__main__':  # DB main testing
    # |✓| 1st Test, create connection
    con = create_con(HOST, USER, PASSWORD, NAME)

    # |✓| 2nd Test, verify DB connection
    if not con.is_connected():
        print("DB connection error!")
    else:
        print("DB connection succeeded!")

    password = 'Pepito123'

    key = createKey(password)

    encrypted = encryptPass(password)

    customEncrypted = customEncrypt(key, password)

    print(key)

    print(encrypted)

    print(bcrypt.checkpw(password.encode(), encrypted))

    print(customEncrypted)

    print(customDecrypt(key,customEncrypted))

    # |✓| 3rd Test, user creation
    create_user(con, 'pepita', 'pepa123')
    create_user(con, 'pepite', 'pepe123')
    create_user(con, 'pepiti', 'pepi123')

    # |✓| 4th Test, verify created user
    if not verify_user(con, "pepito"):
        print("User not found!")
    else:
        print("User found!")

    # |✓| 5th Test, avoid DB duplicates
    create_user(con, 'pep1to', 'pepo123')
    create_user(con, 'p3pito', 'pepo123')

    # |✓| 6th Test, remove users
    delete_user(con, 'pepita')
    delete_user(con, 'pepite')
    delete_user(con, 'pepiti')


