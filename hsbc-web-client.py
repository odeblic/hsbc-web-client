import argparse
import getpass
import logging
import os

from clientfrance import HSBCwebClientFR
from clienthongkong import HSBCwebClientHK

from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
    login = os.environ.get('HSBC_LOGIN')
    password = os.environ.get('HSBC_PASSWORD')

    parser = argparse.ArgumentParser(
        prog='HSBC Web Client',
        description='This script connects to the web interface of HSBC to access online banking services.',
        epilog='Implemented for HK and FR.')

    parser.add_argument('--login')
    parser.add_argument('--password')

    parser.add_argument('--gui', action='store_true', help='Display the GUI')
    parser.add_argument('--verbose', action='store_true', help='Show all log records')
    parser.add_argument('--maximized', action='store_true', help='Maximize the window of the browser')
    parser.add_argument('--hold', action='store_true', help='Do not leave the page after connection')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--hk', action='store_true', help='Select HSBC Hong Kong')
    group.add_argument('--fr', action='store_true', help='Select HSBC France')

    args = parser.parse_args()

    if args.hk:
        Client = HSBCwebClientHK
    elif args.fr:
        Client = HSBCwebClientFR
    else:
        raise RuntimeError('country not specified')

    if args.login is not None:
        login = args.login
    elif os.environ.get('HSBC_LOGIN') is not None and len(os.environ.get('HSBC_LOGIN')) > 0:
        login = os.environ.get('HSBC_LOGIN')
    else:
        login = input("login: ")

    if args.password is not None:
        password = args.password
    elif os.environ.get('HSBC_PASSWORD') is not None and len(os.environ.get('HSBC_PASSWORD')) > 0:
        password = os.environ.get('HSBC_PASSWORD')
    else:
        password = getpass.getpass("password: ")

    client = Client(login, password)
    client.launch(verbose=args.verbose, gui=args.gui, maximized=args.maximized)
    client.open()
    client.logon()
    client.fetch()

    if not args.hold:
        client.logoff()
        client.quit()

