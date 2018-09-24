def logout(driver):
    mouse =driver.find_element_by_xpath(".//*[@class='nav_function']/div[1]/span")
    ActionChains(driver).move_to_element(mouse).perform()
    time.sleep(1)
    # driver.find_element_by_xpath(".//*[@id='qqww']/div[1]/div/ul/li[6]/div[1]/ul/li[7]/a").click()
    driver.find_element_by_link_text("退出登录").click()