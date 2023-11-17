```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EndToEndTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_flow(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        self.assertIn("AI Agent", driver.title)

        # Test user interaction with AI agent
        ai_input = driver.find_element_by_id("user-input")
        ai_input.send_keys("Hello AI")
        ai_input.send_keys(Keys.RETURN)

        # Wait for AI response
        self.wait_for_ai_response()

        # Check AI response
        ai_output = driver.find_element_by_id("ai-output")
        self.assertNotEqual(ai_output.text, "")

        # Test blockchain transaction
        transaction_data = driver.find_element_by_id("transaction-data")
        self.assertNotEqual(transaction_data.text, "")

    def wait_for_ai_response(self):
        import time
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```