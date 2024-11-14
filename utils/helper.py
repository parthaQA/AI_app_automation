from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    email_element = "#username"
    continue_elment = "//span[text()=' Continue ']"
    password_element = "#password"
    login_element = "//span[text()=' Log in ']"
    button_element = ""
    profile_element = ""


    def login(self, sb, user_email, password):
        sb.type(self.email_element, user_email)
        sb.click(self.continue_elment)
        sb.type(self.password_element, password)
        sb.click(self.login_element)


    def verify_sign_out(self, sb):
        return sb.find_element(self.email_element, timeout=5)

    def wait_for_element_presents(self,sb, element):
        wait = WebDriverWait(sb, timeout=15)
        return wait.until(
            EC.visibility_of_all_elements_located(element)
        )
