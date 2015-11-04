from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edit has heard about a cool new online to-do app.
        #She goes to check out the page
        self.browser.get('http://localhost:8000')

        #She notice the page title and header mention To-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #She is invited to add a to-do item stight away

        #She types "Buy peacock feathers" into a text box

        #When she hits enter the page updates and now the page lists
        #"1: Buy peacock feathers" as an item in the to-do list

        #There is still a box inviting her to add another item
        #She enters "Use peacock feathers to make a fly"

        #The page updates again and show both her items

        #Edit wonder whether the list will remeber her list. Then she sees
        #that the site has generated a unique URL for here -- there is some
        #explanatory text to that effect

        #She visits that URL - here to-do list is still there

        #Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')