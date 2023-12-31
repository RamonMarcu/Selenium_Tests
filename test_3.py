# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCompatibilitytestOSGoogleChromeDesktop3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_compatibilitytestOSGoogleChromeDesktop3(self):
    # Test name: Compatibility_test_OS_GoogleChrome_Desktop3
    # Step # | name | target | value
    # 1 | open | https://ramoncristian00.wixsite.com/website | 
    self.driver.get("https://ramoncristian00.wixsite.com/website")
    # 2 | setWindowSize | 2560x1080 | 
    self.driver.set_window_size(2560, 1080)
    # 3 | click | id=DrpDwnMn00label | 
    self.driver.find_element(By.ID, "DrpDwnMn00label").click()
    # 4 | click | id=DrpDwnMn01label | 
    self.driver.find_element(By.ID, "DrpDwnMn01label").click()
    # 5 | runScript | window.scrollTo(0,346) | 
    self.driver.execute_script("window.scrollTo(0,346)")
    # 6 | click | css=.E6d271:nth-child(3) .Dn9jVh | 
    self.driver.find_element(By.CSS_SELECTOR, ".E6d271:nth-child(3) .Dn9jVh").click()
    # 7 | click | css=.XN0hAn > .dBklX7 | 
    self.driver.find_element(By.CSS_SELECTOR, ".XN0hAn > .dBklX7").click()
    # 8 | click | css=.YRSSGK | 
    self.driver.find_element(By.CSS_SELECTOR, ".YRSSGK").click()
    # 9 | click | id=DrpDwnMn02label | 
    self.driver.find_element(By.ID, "DrpDwnMn02label").click()
    # 10 | click | id=DrpDwnMn03label | 
    self.driver.find_element(By.ID, "DrpDwnMn03label").click()
    # 11 | click | id=DrpDwnMn04label | 
    self.driver.find_element(By.ID, "DrpDwnMn04label").click()
    # 12 | mouseOver | id=DrpDwnMn04label | 
    element = self.driver.find_element(By.ID, "DrpDwnMn04label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | id=DrpDwnMn04label | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 14 | click | id=DrpDwnMn05label | 
    self.driver.find_element(By.ID, "DrpDwnMn05label").click()
  
