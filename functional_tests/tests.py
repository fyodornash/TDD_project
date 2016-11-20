from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import sys

class NewVisitorTest(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
    
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
    
    def setUp(self):
        self.browser = webdriver.Firefox(firefox_binary =FirefoxBinary(
        firefox_path = '/home/michael/Downloads/firefox/firefox'))
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #new online to do list app. check out the homepage
        self.browser.get(self.server_url)
        
        #the page title and header mention to do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        
        #she is invited to enter a to do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        

        #when she hits enter the page updates and now the page lists
        #1: Buy peacock feathers as an item in the to do list
        inputbox.send_keys('Buy peacock feathers')
    
        #the text boc to edit is still there after she presses enter
        #and the page updates
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        #There is still a text box inviting her to add another item
        #enters use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        #page updates and shows both items on the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        #now a new user, Francis, comes along to the site
        
        ##We use a new browser session to sure that no information
        ## of ediths is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox(firefox_binary =FirefoxBinary(
        firefox_path = '/home/michael/Downloads/firefox/firefox'))
        
        #francis visits the homepage. there is no sign of ediths list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        #francis starts his own list by entering in a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)        
        
        #francis gets his own unique url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, 'lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)
        
        #Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        #they go to bed happy
        #self.fail('Finish the test!')












































