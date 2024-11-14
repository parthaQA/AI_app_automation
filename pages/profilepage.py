import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase

from utils.helper import Helper

BaseCase.main(__name__, __file__)


class Profile_Page(BaseCase, Helper):
    profile_element = "//span[text()='EU']"
    template_tab_element = "//b[text()='Templates']"
    template_title = (By.CSS_SELECTOR, "div[class='templateNameAndShare']")
    current_template = "//button[@data-pendo-id='selected-template']/parent::div/descendant::div[5]"
    basic_tab = "//b[text()='Basics']"
    sign_out = "//span[text()=' Sign Out ']"
    fingerprint_tab = "//b[text()='Fingerprint']"
    retake_button = "div[class=btn-retake]"
    discover_my_fingerprint_button = "//span[contains(text(),'Discover my fingerprint')]"




    def verify_profile_icon(self, sb):
        return sb.find_element(self.profile_element, timeout=15)

    def click_on_profile(self, sb):
        sb.click(self.profile_element)

    def click_on_template_tab(self,sb):
        sb.click(self.template_tab_element)

    def get_first_five_template_alphabetic_order(self, sb):

        temp = self.wait_for_element_presents(sb, self.template_title)
        list = []

        # Print the text content of each element
        for element in temp:
            list.append(element.text)
        print(sorted(list[:5]))


    def get_current_selected_template(self, sb):
        return sb.find_element(self.current_template, timeout=2).text

    def click_basic_tabs(self,sb):
        sb.click(self.basic_tab)

    def sign_out_from_application(self,sb):
        sb.click(self.sign_out)


    def click_fingerprint_tab(self, sb):
        sb.click(self.fingerprint_tab)

    def click_retake_button(self, sb):
        sb.click(self.retake_button)

    def click_discover_my_fingerprint(self,sb):
        sb.find_element(self.discover_my_fingerprint_button, timeout=15).click()
