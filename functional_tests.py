from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(firefox_binary =FirefoxBinary(
        firefox_path = '/home/michael/Downloads/firefox/firefox'))
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #new online to do list app. check out the homepage
        self.browser.get('http://localhost:8000')
        
        #the page title and header mention to do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        #she is invited to enter a to do item straight away
        #enter a to do list item

        #when she hits enter the page updates and now the page lists
        #1: Buy peacock feathers as an item in the to do list
    
        #the text boc to edit is still there
    
        #enters use peacock feathers to make a fly"

        #page updates and shows both items on the list

        #will the site remember herlist. there is a unique
        #url for each person.

        #at the unique url already created her to do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')












































