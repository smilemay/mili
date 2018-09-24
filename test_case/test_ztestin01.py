import unittest
from test_case.login import login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class Ztestin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        # driver = webdriver.Firefox()
        url = 'http://www.ztestin.com'
        driver.get(url)
        driver.maximize_window()
        cls.driver = driver
    def test_01_login(self):
        self.driver.find_element_by_link_text("登录").click()

        self.driver.find_element_by_id("login_email").send_keys('18899774647')
        self.driver.find_element_by_id("login_password").send_keys('hym19891112')
        self.driver.find_element_by_xpath(".//*[@id='btn_submit1989']/button").click()
    def test_02_select_tpye(self):
        self.driver.find_element_by_xpath(".//*[@id='qqww']/div[1]/div/ul/li[1]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='qqww']/div[4]/div[1]/div[1]/ul[1]/li[4]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='qqww']/div[4]/div[1]/div[2]/ul/li[1]/a/ul").click()

    def test_03_logout(self):
        mouse = self.driver.find_element_by_xpath(".//*[@class='nav_function']/div[1]/span")
        ActionChains(self.driver).move_to_element(mouse).perform()
        time.sleep(1)
        # driver.find_element_by_xpath(".//*[@id='qqww']/div[1]/div/ul/li[6]/div[1]/ul/li[7]/a").click()
        self.driver.find_element_by_link_text("退出登录").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ =='__main__':
    unittest.main()