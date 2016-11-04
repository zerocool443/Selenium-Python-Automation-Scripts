from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
i = 2 # do it 2 times
while i > 0:
    driver = webdriver.Chrome()
    driver.get("https://academia.srmuniv.ac.in")

    def find_by_xpath(locator):
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

        return element

    class FormPage(object):
        def fill_form(self, data):
            find_by_xpath('//*[@id="Email"]').send_keys(data['username'])
            find_by_xpath('//*[@id="Password"]').send_keys(data['password'])

            return self # makes it so you can call .submit() after calling this function

        def submit(self):
            find_by_xpath('//input[@value = "Submit"]').click()

    data = {
        'username': 'user',
        'password': 'user'
    }

    FormPage().fill_form(data).submit()
    driver.quit() # closes the webbrowser
    i = i - 1