from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
     

class LayoutAndStylingTest(FunctionalTest):

    
    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)
        
        #she notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            512,
            delta= 5
        )
        #she starts a list and notices that the input box is
        #still nicely centered.
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] /2,
            512,
            delta = 5
        )



























