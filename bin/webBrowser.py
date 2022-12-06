#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 12/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Login Screen """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver import *
import requests
import webbrowser
import settings


def set_browser(browser):
    match browser:
        case 'Firefox':
            web_browser = webdriver.Firefox
        case 'Chrome':
            web_browser = webdriver.Chrome
        case 'Safari':
            web_browser = webdriver.Safari
        case _:
            web_browser = webdriver.Edge
    settings.__browser__ = web_browser


def get_browser():
     browser = webbrowser.get()
     print(browser.__class__)
     if browser.__class__ == "":
        set_browser()
     else:
        set_browser(browser.__class__)


def checkURL(url):
    try:
        req = requests.get(url)
        while req.status_code != requests.codes['ok']:
            return checkURL(input('Please enter a valid url:'))
    except Exception as ex:
        print(f'Something went wrong: {ex}')
        print('Try again!')
        return checkURL(input('Please enter a valid url:'))

    return url


def access_account(username, password, url):
    try:
        if settings.__browser__ == "":
            get_browser()
    except AttributeError:
        print('No WebBrowser found')
        set_browser('')

    settings.__browser__.get(url)


