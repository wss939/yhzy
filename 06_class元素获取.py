import unittest

import time
from selenium import webdriver


class Y(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.host="http://127.0.0.1"

    def test_by_class(self):
        self.driver.get(self.host+"/SeleniumDemo/elements.html")
        input3=self.driver.find_element_by_class_name("input3")
        input3.clear()
        input3.send_keys("sssss")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
