import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UiPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def search_by_phrase(self, phrase: str):
        self.driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def search_by_author(self, author_name: str):
        self.driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(author_name)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def add_to_cart(self, book_name: str):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "product-title__head"))
        )
        search_box.send_keys(book_name)
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        search_button.click()
        buy_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "action-button__text='Купить']"))
        )
        buy_button.click()
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "action-button__text='Оформить']"))
        )
        cart_icon.click()
    # падает с ошибкой TimeoutException


    def add_to_cart(self, book_name: str):
        self.driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(book_name)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.driver.find_element(By.CSS_SELECTOR, "action-button__text='Купить']").click()
        self.driver.find_element(By.CSS_SELECTOR, "action-button__text='Оформить']").click()

    # падает с ошибкой InvalidSelectorException

# (By.NAME, "phrase")