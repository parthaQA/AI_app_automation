import pytest
from seleniumbase import BaseCase
from config.config_helper import login_cred
from pages.autogenerator import AutoGenerator
from pages.profilepage import Profile_Page
from pages.slidespage import Slides_Page
from utils.helper import Helper


class Test_prezent_ai_cases(BaseCase):
    profile_page = Profile_Page()
    helper = Helper()
    slide_page = Slides_Page()
    auto_generator = AutoGenerator()

    def setUp(self):
        super().setUp()
        self.open(login_cred["url"])
        print("browser launched")
        self.maximize_window()
        self.helper.login(self, login_cred["email"], login_cred["password"])

    def tearDown(self):
        try:
            self.assert_true(self.profile_page.verify_profile_icon(self))
            self.profile_page.click_on_profile(self)
            self.profile_page.click_basic_tabs(self)
            self.profile_page.sign_out_from_application(self)
            self.assert_true(self.helper.verify_sign_out(self))
            super().tearDown()
        finally:
            super().tearDown()
            print("browser closed")

    @pytest.mark.alphabetic_order
    def test_get_first_five_template_alphabetic_order(self):
        self.assert_true(self.profile_page.verify_profile_icon(self))
        self.profile_page.click_on_profile(self)
        self.profile_page.click_on_template_tab(self)
        self.profile_page.get_first_five_template_alphabetic_order(self)
        print("first five template is printed in alphabetic order")
        print(self.profile_page.get_current_selected_template(self))

    @pytest.mark.retake_fingerprints
    def test_retake_fingerprints(self):
        self.assert_true(self.profile_page.verify_profile_icon(self))
        self.profile_page.click_on_profile(self)
        self.profile_page.click_fingerprint_tab(self)
        self.profile_page.click_retake_button(self)
        self.profile_page.click_discover_my_fingerprint(self)
        self.slide_page.select_card_item(self, "2")
        self.slide_page.verify_fingerprint_is_generated(self)
        print("fingerprint has generated")
        self.slide_page.navigate_back_to_prezent(self)

    @pytest.mark.download_generated_ppt
    def test_create_and_download_generated_ppt(self):
        self.auto_generator.click_auto_generator(self)
        self.auto_generator.click_prompt_text_area(self)
        self.auto_generator.select_third_suggestion(self)
        self.auto_generator.generate_slide(self)
        self.assert_true(self.auto_generator.get_generated_slide(self))
        print("slide has generated")
        self.auto_generator.add_slide_to_favourite(self)
        self.assert_true(self.auto_generator.download_generated_ppt(self))
        print("slide has downloaded")



