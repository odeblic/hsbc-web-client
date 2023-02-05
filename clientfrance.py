import os
import time

from clientbase import HSBCwebClient

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HSBCwebClientFR(HSBCwebClient):
    def __init__(self, *args, **kwargs):
        URL = 'https://www.hsbc.fr/1/2//hsbc-france/particuliers/connexion'
        super().__init__(URL, *args, **kwargs)

    def logon(self):
        WebDriverWait(self._driver, 5).until(EC.title_contains("Connexion espace client - Ma Banque en ligne | HSBC"))
        self._logger.debug(f'loaded page: "{self._driver.title}"')

        try:
            WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable((By.ID, "consent_prompt_decline"))).click()
            self._logger.debug("refuse cookies")
        except:
            pass

        element = WebDriverWait(self._driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='ident']")))
        element.send_keys(self._login)
        element.submit()
        self._logger.debug("user name submitted") 

        WebDriverWait(self._driver, 5).until(EC.title_contains("HSBC: Ma Banque en ligne"))
        self._logger.debug(f'loaded page: "{self._driver.title}"')

        time.sleep(4)
        elements = self._driver.find_elements("xpath", "//a")
        for element in elements:
            if element.get_attribute("innerText") == 'Password':
                element.click()
                self._logger.debug("password selected")
                break

        time.sleep(4)
        element = WebDriverWait(self._driver, 15).until(EC.presence_of_element_located((By.ID, "memorableAnswer")))
        self._logger.debug("found element: memorableAnswer")

        element.send_keys('claquettes')
        self._logger.debug("question submitted") 

        time.sleep(4)
        element = self._driver.find_element("xpath", "//ul[contains(@class, 'code')]")
        subelements = element.find_elements("xpath", ".//li")

        index = 0
        indices = []

        for subelement in subelements:
            html = subelement.get_attribute("innerHTML")
            if html.startswith('<input '):
                if "disabled" not in html:
                    indices.append(index)
                index = index + 1
            elif html.startswith('<span '):
                index = -2

        element = self._driver.find_element("id", "keyrcc_password_first1")
        element.send_keys(self._password[indices[0]])

        element = self._driver.find_element("id", "keyrcc_password_first2")
        element.send_keys(self._password[indices[1]])

        element = self._driver.find_element("id", "keyrcc_password_first3")
        element.send_keys(self._password[indices[2]])

        element.submit()

    def fetch(self):
        # WebDriverWait(self._driver, 15).until(EC.title_contains("comptes | HSBC"))
        time.sleep(10)
        self._logger.debug(f'loaded page: "{self._driver.title}"')
        self._logger.info("stage FETCHING")
        self._screenshot('accounts-fr.png')
        self._print('accounts-fr.pdf')

    def logoff(self):
        pass
