import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Diploma.Diploma.pages.ui_page import UiPage
from settings import ui_url


@allure.feature("Тестирование интернет-магазина")
@allure.title("Позитивные тесты.UI")
@allure.severity("blocker")
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
@allure.severity("blocker")
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
@allure.severity("blocker")
@allure.step("Добавить книгу в корзину")
@pytest.mark.parametrize("book_name",
                         ["Дневник книготорговца", "трое в лодке не считая собаки", "1984", "Sailor moon", "Соня"])
def test_add_to_cart(book_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Получить результаты добавления в корзину"):
        add_to_cart = driver.find_element(By.NAME, "phrase")
    with allure.step("Проверить, что корзина не пуста"):
        assert add_to_cart is not None
    with allure.step("Закрыть браузер"):
        driver.quit()

@allure.feature("Тестирование интернет-магазина")
@allure.title("Негативные тесты.UI")
@allure.severity("blocker")
@allure.step("Добавить книгу в корзину с невалидным названием")
@pytest.mark.parametrize("book_name", ["___", "$^&*", ";)", "😁"])
def test_add_to_cart_negative(book_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Получить результаты добавления в корзину"):
        add_to_cart = driver.find_element(By.NAME, "phrase")
    with allure.step("Проверить, что ничего не найдено"):
        assert ui_page.found_nothing() == "Похоже, у нас такого нет"
    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.feature("Тестирование интернет-магазина")
@allure.title("Позитивные тесты.UI")
@allure.step("Удаление товара из корзины")
@allure.severity("BLOCKER")
@pytest.mark.parametrize("book_name", ["Умная собачка Соня"])
def test_delete_from_cart(book_name):
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
    with allure.step("Перейти на сайт Читай-город"):
        ui_page = UiPage(driver, ui_url)
    with allure.step("Добавить книгу в корзину"):
        ui_page.add_to_cart(book_name)
    with allure.step("Перейти в корзину и удалить книгу"):
        ui_page.delete_from_cart(book_name)
    with allure.step("Проверить, что товар больше не существует в списке"):
        cart_items = driver.find_elements(By.CSS_SELECTOR, "cart-multiple-delete")
        assert all(
            book_name not in element.text for element in cart_items), f"Книга '{book_name}' еще в корзине"
    with allure.step("Закрыть браузер"):
        driver.quit()
