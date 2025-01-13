import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Diploma.Diploma.pages.ui_page import UiPage
from settings import ui_url


@allure.feature("Тестирование интернет-магазина")
@allure.title("Позитивные тесты.UI")
@allure.step("Найти книгу по заголовку")
@pytest.mark.parametrize("book_name", ["Кот", "1984", "python", "Сейлор Мун"])
def test_search_by_phrase(book_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Найти книгу по заголовку"):
        ui_page.search_by_phrase(book_name)
    with allure.step("Закрыть браузер"):
        driver.quit()

@allure.feature("Тестирование интернет-магазина")
@allure.title("Позитивные тесты.UI")
@allure.step("Найти книгу по автору")
@pytest.mark.parametrize("author_name", ["Кант", "Салтыков-Щедрин", "Romain", "Федерико Гарсия Лорка"])
def test_search_by_author(author_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Найти книгу по автору"):
        ui_page.search_by_author(author_name)
    with allure.step("Закрыть браузер"):
        driver.quit()

@allure.feature("Тестирование интернет-магазина")
@allure.title("Позитивные тесты.UI")
@allure.step("Добавить книгу в корзину")
@pytest.mark.parametrize("book_name", ["Дневник книготорговца"])
def test_add_to_cart(book_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Добавить в корзину книгу"):
        ui_page.add_to_cart(book_name)
    with allure.step("Получить результаты добавления в корзину"):
        try:
            add_to_cart = driver.find_element(By.NAME, "phrase")
        except NoSuchElementException:
            allure.attach(driver.page_source, "Page Source")
            raise AssertionError("Элемент не найден на странице")
    with allure.step("Проверить, что корзина не пуста"):
        assert add_to_cart is not None
    with allure.step("Закрыть браузер"):
        driver.quit()


#     with allure.step("Перейти в корзину"):
#         ui_page.go_to_cart()
#     with allure.step("Получить результаты добавления в корзину"):
#         results_add = driver.find_element(By.CSS_SELECTOR, 'div.product-title__head')
#     with allure.step("Проверить, что корзина не пуста"):
#         assert results_add is not None
#     with allure.step("Закрыть браузер"):
#         driver.quit()

# def test_search_zero():
#     with allure.step("Пустой запрос в поиске. Negative"):
#         driver = webdriver.Chrome()
#         zero = " "
#         driver.get(zero)