from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_tpye(driver):
    driver.find_element_by_xpath(".//*[@id='qqww']/div[1]/div/ul/li[1]/a").click()
    driver.find_element_by_xpath(".//*[@id='qqww']/div[4]/div[1]/div[1]/ul[1]/li[4]/a").click()
    driver.find_element_by_xpath(".//*[@id='qqww']/div[4]/div[1]/div[2]/ul/li[1]/a/ul").click()
if __name__ == '__main__':
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    select_tpye(driver)