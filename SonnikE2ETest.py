import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Открыть сайт
driver.get("https://horo.mail.ru/sonnik/")
i = 1
while i < 30:
    btn_letter = driver.find_element(By.CSS_SELECTOR, "a:nth-of-type(" + str(i) + ") > .filter__text")
    time.sleep(1)
    btn_letter.click()
    k = 0
    j = 1
    while k < 1:
        btn_form = driver.find_element(By.CSS_SELECTOR,
                                       ".p-terms-list > div > a:nth-of-type(" + str(j) + ") > .link__text")
        time.sleep(1)
        btn_form.click()
        interpret = driver.find_element(By.CSS_SELECTOR, "div p").get_property("textContent")
        print(i, "/", j, " [ ", interpret, " ]")
        driver.get("https://horo.mail.ru/sonnik/")
        btn_letter = driver.find_element(By.CSS_SELECTOR, "a:nth-of-type(" + str(i) + ") > .filter__text")
        time.sleep(1)
        btn_letter.click()
        if driver.find_element(By.CSS_SELECTOR,
                               ".p-terms-list > div > a:nth-of-type(" + str(
                                   j) + ") > .link__text") == driver.find_element(By.CSS_SELECTOR,
                                                                                  ".p-terms-list > div > "
                                                                                  "a:last-of-type > .link__text"):
            k = 2
        j += 1
    i += 1
