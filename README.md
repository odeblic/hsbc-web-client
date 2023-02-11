# HSBC Web Client

### Description

This module written in Python3 simply connects to the HSBC online banking web page and fetches the list of your accounts with their balance.

It connects to the bank's portal of the selected country, fills the HTML forms automatically with given credentials, and fetches the account details.

The information is stored in files with the following formats:

+ PNG (browser screenshot)
+ PDF (saved web page)
+ CSV (parsed account list)

### Requirements

You need **Python3** installed with modules **selenium** and **webdriver-manager**.

```bash
pip3 install -r requirements.txt
```

Of course, you need a legit HSBC account (with credentials for online banking)
either in France or Hong Kong.

### Usage

```bash
usage: HSBC Web Client [-h] [--login LOGIN] [--password PASSWORD] [--gui]
                       [--verbose] [--maximized] [--hold] (--hk | --fr)

This script connects to the web interface of HSBC to access online banking
services.

optional arguments:
  -h, --help           show this help message and exit
  --login LOGIN
  --password PASSWORD
  --gui                Display the GUI
  --verbose            Show all log records
  --maximized          Maximize the window of the browser
  --hold               Do not leave the page after connection
  --hk                 Select HSBC Hong Kong
  --fr                 Select HSBC France

Implemented for HK and FR.
```

On the first run using the `--gui` option is probably going to be necessary 
so the browser can be trusted and/or a one time password (OTP) can be sent.

You can simply run the program as follow:

```bash
python3 hsbc-web-client.py
```

However, you might appreciate the provided Makefile to avoid repetitive work.

You must first indicate your credentials in the file `credentials.mk`:

```make
# credentials for your account in Hong Kong
LOGIN_HK=myself
PASSWORD_HK=********

# credentials for your account in France
LOGIN_FR=myself
PASSWORD_FR=********
```

Then, you must setup the environment for the country you want:

```bash
# environment for HSBC Hong Kong
eval `make env.hk`
```

```bash
# environment for HSBC France
eval `make env.fr`
```

Finally, you can invoke the target to run the program:

```bash
# run with the GUI in verbose mode and do not quit after logon
make debug

# run with no GUI in background and generate the report silently
make run
```

Other targets are available:

```bash
# install the program locally in the home directory
make install

# cleanup the files produced by runs or builds
make clean
```

#### Using an ini configuration file

There is also an example of using an ini file: `hsbc.ini.example`.  
ou can look at `hsbc-web-client.py` for more details on how to use.

# Disclaimer

All of this is just a demo and nothing else. It is not deliverable!

The code may break easily since the web portal may be updated anytime.

Your credentials are not protected since they are not encrypted
and appear in clear in the terminal.

# Warranty

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar.

See [www.wtfpl.net](http://www.wtfpl.net/) for more details.

# License

This program is distributed under the [WTFPL](http://www.wtfpl.net/) license.

Copyright © 2023 Your Name <odeblic@gmail.com>

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.

# Author

A guy who wishes that everything can be accessed through an API,
hence this project...

[Olivier de BLIC](mailto:odeblic@gmail.com)

# Contributors

[Andrew Lister](mailto:a.lister.hk@gmail.com)

> "Please do not do shady things with my code.
You must be the owner of the account you are using."

