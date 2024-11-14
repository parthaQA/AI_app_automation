import time

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

from utils.helper import Helper

BaseCase.main(__name__, __file__)


class Slides_Page(BaseCase, Helper):
    slide_element = "//div[text()='Which slide do you like more?']"
    card_items = (By.XPATH, "//div[@class='card-item']")
    second_item = "//div[@class='card-item']/following::div[5]"
    common_pref_text = "//div[contains(text(), 'Select from common preferences')]"
    choose_template = "//span[contains(text(), 'Start with an Executive Summary')]"
    next_button = "//span[contains(text(),'Next')]"
    fingerprint_tab = "//b[text()='Fingerprint']"
    retake_button = "div[class=btn-retake]"
    discover_my_fingerprint_button = "//span[contains(text(),'Discover my fingerprint')]"
    choose_industry = "//div[contains(text(),'Chemical')]"
    skip_button = ".skip-button"
    view_fingerprint = "//span[contains(text(),'View my fingerprint')]"
    generated_fingerprint = "span.highlight"
    back_to_prezent_button = "//span[contains(text(),'Back to Prezent')]"

    def verify_slide_page(self, sb):
        sb.find_element(self.slide_element, timeout=2)

        # Print the text content of each element

    def select_card_item(self, sb, value):
        # get_attibute = sb.get_attribute(self.second_item, "style")
        # print("get_attibute " + get_attibute)
        selected_option = "//div[@class='images-wrapper']/child::div[" + value + "]"
        while True:
            sb.wait(20)
            if sb.is_element_visible(selected_option):
                temp = self.wait_for_element_presents(sb, self.card_items)
                print(f'count of card item is : {len(temp)}')
                get_attibute = sb.get_attribute(self.second_item, "style")
                print("get_attibute " + get_attibute)
                sb.click(selected_option, timeout=25)

            if sb.is_element_visible(self.choose_template):
                # sb.wait(20)
                sb.wait_for_element_clickable(self.choose_template, timeout=30)
                sb.click(self.choose_template)
                sb.click(self.next_button)
                sb.click(self.choose_industry, timeout=5)
                sb.click(self.next_button)

            if sb.is_element_present(self.skip_button):
                sb.click(self.skip_button, timeout=15)
                sb.wait(10)
                if sb.is_element_present(self.view_fingerprint):
                    sb.click(self.view_fingerprint, timeout=20)
                    break

    def verify_fingerprint_is_generated(self, sb):
        get_name = sb.find_element(self.generated_fingerprint, timeout=10)
        print(get_name.text)

    def navigate_back_to_prezent(self,sb):
        sb.find_element(self.back_to_prezent_button)
        sb.click(self.back_to_prezent_button)
