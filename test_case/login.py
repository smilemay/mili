from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def login(driver,username,password):
    driver.find_element_by_link_text("登录").click()

    driver.find_element_by_id("login_email").send_keys(username)
    driver.find_element_by_id("login_password").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='btn_submit1989']/button").click()



if __name__ == '__main__':
    driver =webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    url = "https://www.ztestin.com/"
    driver.get(url)
    driver.implicitly_wait(20)
    driver.maximize_window()
    login(driver,'18899774647','hym19891112')
    time.sleep(3)
    driver.quit()
