import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UiPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.chitai-gorod.ru/")

    def set_cookie_policy(self):
        cookie = {
            'name': 'access-token',
            'value': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMzc0MDQ5LCJpYXQiOjE3MzYzMzQ1MjIsImV4cCI6MTczNjMzODEyMiwidHlwZSI6MjB9.b4Zwm2yxE1trGNtFunDbaAJ3PeBwxRbfI6hMJ8Xynoo'
        }
        self.driver.add_cookie(cookie)

    def search_by_title(self,term):
        self.driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()