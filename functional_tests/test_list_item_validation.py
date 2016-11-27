from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #edith goes to the home page and accidentally tries to submit
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        #an empty list item. She hits enter on the empty input box
        
        #the home page refreshes, and there is an error message saying that the 
        #list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #she tries again with some text for the item which works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.assertEqual(error.text,"You can't have an empty list item")
        
        #perversely, she now decides to submit a second blank item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        #she receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #and she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        













































