from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

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
        self.browser.get('http://localhost:8000')
        
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
        
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        #There is still a text box inviting her to add another item
        #enters use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        #page updates and shows both items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly', [row.text for row in rows]
        )
        #will the site remember herlist. there is a unique
        #url for each person.

        #at the unique url already created her to do list is still there.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')












































