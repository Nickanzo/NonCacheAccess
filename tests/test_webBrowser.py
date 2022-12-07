from selenium import webdriver
from selenium.webdriver.edge.service import Service

if __name__ == '__main__':

    PATH = "..\\webDrivers\\Edge\\msedgedriver.exe"

    service = Service(PATH)
    browser = webdriver.Edge(service=service)

