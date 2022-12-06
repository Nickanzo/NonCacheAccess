#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Settings file for general data used along the app"""
# ---------------------------------------------------------------------------
# Database Config
# ---------------------------------------------------------------------------
# HOST = 'sql10.freesqldatabase.com'
HOST = 'localhost'
# NAME = 'sql10519450'
NAME = 'noncacheaccess'
# USER = 'sql10519450'
USER = 'admin'
# PASSWORD = 'JFQ1m2LHKs'
PASSWORD = 'admin'
PORT = '3306'
# ---------------------------------------------------------------------------
# Window definitions
# ---------------------------------------------------------------------------
MAIN_SIZE = '1100x580'
HEIGHT = 580
WIDTH = 1100
THEME = 'Light'
TEXT_FIELDS = '#e0e6e9'
REGISTER_FIELDS = '#fbf1ef'
BACKGROUND = '#b47eb3'
# ---------------------------------------------------------------------------
# Global Data
# ---------------------------------------------------------------------------
global __user__
global __browser__
global __con__


# ---------------------------------------------------------------------------
# Initialization
# ---------------------------------------------------------------------------
def init():
    global __user__
    global __con__
    #global __browser__
    __user__ = ''
    __con__ = ''
    #__browser__ = ''



