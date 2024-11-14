from seleniumbase import BaseCase

from utils.helper import Helper


class AutoGenerator(BaseCase, Helper):
    auto_generator = "div[style^='transform']"
    enter_prompt_area = "textarea[data-pendo-id='generate-propmt']"
    third_suggestion = "#generate-suggested-2"
    generate_button = "//span[contains(text(),'Generate')]"
    download_icon = "span[name='download-icon']"
    favourite_icon = "i[name='favorite-icon']"
    generated_slide = "div[data-pendo-id='generated-slide']"
    generated_action_modal = ".generateActionModalContainer"
    generated_favorites = "//span[contains(text(), 'Add to Favorites')]"
    added_to_fav = "//span[contains(text(), 'Added to Favorites')]"
    close_modal = ".closeIconContainer"
    download_container = "//div[contains(text(),'Download Prezentation')]"
    download_button = "[id='download-btn'] span div"
    download_as_ppt = "//*[contains(text(),'Download as pptx')]"
    download_complete = "//span[contains(text(),'Download Completed')]"

    def click_auto_generator(self, sb):
        sb.find_element(self.auto_generator, timeout=10)
        sb.click(self.auto_generator)

    def click_prompt_text_area(self, sb):
        sb.find_element(self.enter_prompt_area, timeout=10)
        sb.click(self.enter_prompt_area)


    def select_third_suggestion(self, sb):
        get_text = sb.find_element(self.third_suggestion, timeout=10)
        print("printing the text of third suggestion : ", get_text.text)
        sb.click(self.third_suggestion)


    def generate_slide(self,sb):
        sb.find_element(self.generate_button, timeout=10)
        sb.click(self.generate_button)

    def get_generated_slide(self,sb):
        sb.find_element(self.generated_slide, timeout=180)
        return sb.is_element_visible(self.generated_slide)

    def add_slide_to_favourite(self,sb):
        sb.find_element(self.favourite_icon)
        sb.click(self.favourite_icon)
        if sb.is_element_visible(self.generated_action_modal):
            sb.click(self.generated_favorites, timeout=2)
        try:
            sb.find_element(self.added_to_fav,timeout=8)
        except:
            print(f'{self.added_to_fav} element not found')
        sb.assert_true(sb.is_element_visible(self.added_to_fav))
        sb.click(self.close_modal, timeout=3)

    def download_generated_ppt(self, sb):
        sb.find_element(self.download_icon, timeout=2)
        sb.click(self.download_icon)
        if sb.is_element_visible(self.download_container):
            sb.click(self.download_button, timeout=2)
        sb.find_element(self.download_as_ppt, timeout=3)
        sb.click(self.download_as_ppt)
        sb.find_element(self.download_complete, timeout=15)
        return sb.is_element_visible(self.download_complete)







