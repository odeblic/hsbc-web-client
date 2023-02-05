-include credentials.mk

.PHONY: env.hk env.fr debug clean install run

env.hk:
	@printf "export HSBC_COUNTRY=hk\n"
	@printf "export HSBC_LOGIN=$(LOGIN_HK)\n"
	@printf "export HSBC_PASSWORD=$(PASSWORD_HK)\n"

env.fr:
	@printf "export HSBC_COUNTRY=fr\n"
	@printf "export HSBC_LOGIN=$(LOGIN_FR)\n"
	@printf "export HSBC_PASSWORD=$(PASSWORD_FR)\n"

debug:
	@[ "$(HSBC_COUNTRY)" = hk -o "$(HSBC_COUNTRY)" = fr ] || (printf "HSBC_COUNTRY must be set to either 'hk' or 'fr'\n" && false)
	python3 hsbc-web-client.py --$(HSBC_COUNTRY) --gui --verbose --hold

clean:
	# rm -fr /tmp/* > /dev/null 2>&1 ; true
	rm -fr build dist HSBC_Web_Client.egg-info
	rm -fr __pycache__ geckodriver.log
	rm -f accounts-hk.png accounts-hk.pdf accounts-hk.csv
	rm -f accounts-fr.png accounts-fr.pdf accounts-fr.csv

install:
	python3 setup.py install --prefix ~/.local

run:
	@[ "$(HSBC_COUNTRY)" = hk -o "$(HSBC_COUNTRY)" = fr ] || (printf "HSBC_COUNTRY must be set to either 'hk' or 'fr'\n" && false)
	python3 -m hsbc-web-client --$(HSBC_COUNTRY)

