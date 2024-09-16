import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Настраиваем драйвер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем сайт и авторизуемся
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Выбор товара
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Переход в корзину и проверка товара
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(2)
assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack", "Товар не добавлен в корзину"

# Оформление покупки
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "last-name").send_keys("User")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Завершение покупки
driver.find_element(By.ID, "finish").click()
time.sleep(2)
assert driver.find_element(By.CLASS_NAME, "complete-header").text == "THANK YOU FOR YOUR ORDER", "Покупка завершена успешно"

# Закрываем браузер
driver.quit()
