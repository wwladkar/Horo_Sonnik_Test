import time  # Подключение модуля для работы со временем
from selenium import webdriver  # Подключение пакета selenium webdriver для управления браузером
from selenium.webdriver.common.by import By  # Подключение модуля для поиска элементов на странице
from selenium.webdriver.chrome.service import Service as ChromeService  # Подключение класса, отвечающего за старт
# и остановку webdriver
from webdriver_manager.chrome import ChromeDriverManager  # Подключение менеджера автоматического обновления webdriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Инициализация webdriver через
# менеджер обновлений

driver.get("https://horo.mail.ru/sonnik/")  # Открытие тестируемого сервиса
i = 1  # Объявление переменной для входа в цикл с начальным значением
while i < 30:  # Цикл перебора всех 29-ти букв-ссылок поочередно
    btn_letter = driver.find_element(By.CSS_SELECTOR, "a:nth-of-type(" + str(i) + ") > .filter__text")  # Поиск элемента
    time.sleep(1)  # Задержка времени в 1 секунду перед кликом для прогрузки странички
    btn_letter.click()  # Клик по элементу
    k = 0  # Объявление переменной для входа в цикл с начальным значением
    j = 1  # Объявление переменной для входа в цикл с начальным значением
    while k < 1:  # Цикл перебора всех образов-ссылок на выбранную букву поочередно до последнего
        btn_form = driver.find_element(By.CSS_SELECTOR,  # Поиск элемента
                                       ".p-terms-list > div > a:nth-of-type(" + str(j) + ") > .link__text")
        time.sleep(1)  # Задержка времени в 1 секунду перед кликом для прогрузки странички
        btn_form.click()  # Клик по элементу
        interpret = driver.find_element(By.CSS_SELECTOR, "div p").get_property("textContent")  # Поиск содержимого тега
        print(i, "/", j, " [ ", interpret, " ]")  # Вывод в консоль порядкового номера буквы, образа и содержимого
        driver.get("https://horo.mail.ru/sonnik/")  # Возврат в изначальное состояние перед циклом перебора образов
        btn_letter = driver.find_element(By.CSS_SELECTOR, "a:nth-of-type(" + str(i) + ") > .filter__text")  # Поиск эл.
        time.sleep(1)  # Задержка времени в 1 секунду перед кликом для прогрузки странички
        btn_letter.click()  # Клик по элементу
        if driver.find_element(By.CSS_SELECTOR,  # Проверка условия выхода из цикла (если выбранный элемент последний)
                               ".p-terms-list > div > a:nth-of-type(" + str(
                                   j) + ") > .link__text") == driver.find_element(By.CSS_SELECTOR,
                                                                                  ".p-terms-list > div > "
                                                                                  "a:last-of-type > .link__text"):
            k = 2  # Присвоение переменной значения для выхода из цикла, если условие верно
        j += 1  # Приращение переменной цикла перебора образов
    i += 1  # Приращение переменной цикла перебора букв
