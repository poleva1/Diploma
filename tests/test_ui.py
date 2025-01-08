from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest

from Diploma.Diploma.pages.ui_page import UiPage
from settings import ui_url

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_search_by_title():
    with allure.step("Найти книгу по заголовку"):
        driver = webdriver.Chrome()
        title = "Книготорговец"
        driver.get(title)

def test_search_by_author():
    with allure.step("Найти книгу по автору"):
        driver = webdriver.Chrome()
        book_author = "Байтелл"
        driver.get(book_author)

def test_add_to_cart():
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(ui_url)

    with allure.step("Добавить в корзину книгу с названием 'Книготорговец'"):
        book_title = "Книготорговец"
        driver = add_to_cart(book_title)

    with allure.step("Получить результаты добавления в корзину"):
        results_add = driver.find_element(By.CSS_SELECTOR, 'div.product-title__head')

    with allure.step("Проверить, что корзина не пуста"):
        assert results_add is not None

    with allure.step("Закрыть браузер"):
        driver.quit()