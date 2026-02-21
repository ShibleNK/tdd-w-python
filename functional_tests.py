from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class newVisitorTest(unittest.TestCase):
    def setUp(self):
        


        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument(
            "--disable-dev-shm-usage"
        )  # Overcomes some limitations in a shared env
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        
        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        [...]
        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()