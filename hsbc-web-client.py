import argparse
import getpass
import logging
import os
import sys

from hsbc_web_client.clienthongkong import HSBCwebClientHK
from hsbc_web_client.clientfrance import HSBCwebClientFR

import configparser


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")

    inifile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),
                           "hsbc.ini")
    if os.path.exists(inifile):
        config = configparser.ConfigParser()
        config.read(inifile)
        login = config.get('DEFAULT', 'login')
        password = config.get('DEFAULT', 'password')
        country = config.get('DEFAULT', 'country')
        gui = config.getboolean('DEFAULT', 'gui')
        maximized = config.getboolean('DEFAULT', 'maximized')
        hold = config.getboolean('DEFAULT', 'hold')
        verbose = config.getboolean('DEFAULT', 'verbose')
    else:
        login = os.environ.get('HSBC_LOGIN')
        password = os.environ.get('HSBC_PASSWORD')
        country = None

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

    if not os.path.exists(inifile):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--hk',action='store_true', help='Select HSBC Hong Kong')
        group.add_argument('--fr', action='store_true', help='Select HSBC France')

    args = parser.parse_args()

    if (hasattr(args, "hk") and args.hk) or country == "hongkong":
        Client = HSBCwebClientHK
    elif (hasattr(args, "fr") and args.fr) or country == "france":
        Client = HSBCwebClientFR
    else:
        raise RuntimeError('country not specified')

    if args.login is not None:
        login = args.login
    elif os.environ.get('HSBC_LOGIN') is not None and len(os.environ.get('HSBC_LOGIN')) > 0:
        login = os.environ.get('HSBC_LOGIN')
    elif not login:
        login = input("login: ")

    if args.password is not None:
        password = args.password
    elif os.environ.get('HSBC_PASSWORD') is not None and len(os.environ.get('HSBC_PASSWORD')) > 0:
        password = os.environ.get('HSBC_PASSWORD')
    elif not password:
        password = getpass.getpass("password: ")

    client = Client(login, password)
    client.launch(verbose=args.verbose, gui=args.gui, maximized=args.maximized)
    client.open()
    client.logon()
    client.get_account_info()
    client.fetch()

    if not args.hold:
        client.logoff()
        client.quit()

