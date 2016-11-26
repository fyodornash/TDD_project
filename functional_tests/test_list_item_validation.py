from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #edith goes to the home page and accidentally tries to submit
        #an empty list item. She hits enter on the empty input box
        
        #the home page refreshes, and there is an error message saying that the 
        #list items cannot be blank
        
        #she tries again with some text for the item which works
        
        #perversely, she now decides to submit a second blank item
        
        #she receives a similar warning on the list page
        
        #and she can correct it by filling some text in
        
        self.fail('Finish the test!')












































