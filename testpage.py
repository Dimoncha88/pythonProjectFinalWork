import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators:
    ids = dict()
    with open('./locator.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)

    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()


# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word)

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word)


# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'])

    def click_about_link(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_ABOUT_LINK'])


# GET PROPERTY
    def get_header_size(self):
        header_size = self.get_element_property(TestSearchLocators.ids['LOCATOR_ABOUT_HEADER_SIZE'], 'Margin')
        return header_size.split()[0]
