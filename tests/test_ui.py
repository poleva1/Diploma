import allure
import pytest
from selenium import webdriver
from Diploma.Diploma.pages.ui_page import UiPage
from Diploma.settings import ui_url

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    ui_page = UiPage(driver, ui_url)
    yield ui_page
    driver.quit()


@allure.feature("Тестирование интернет-магазина")
@allure.story("Позитивные тесты.UI")
@allure.severity("blocker")
@allure.title("Найти книгу по заголовку")
@pytest.mark.parametrize("book_name", ["Три мушкетера",
                                       "1984",
                                       "Умная собачка Соня"])
def test_search_by_phrase(browser, book_name):
    with allure.step(f"Поиск книг с названием"
                     f" {book_name}"):
        browser.search_by_phrase(book_name)

    with allure.step(f"Книга с названием {book_name} найдена"):
        assert book_name in browser.find_book_titles()


@allure.feature("Тестирование интернет-магазина")
@allure.story("Позитивные тесты.UI")
@allure.severity("blocker")
@allure.title("Найти книгу по автору")
@pytest.mark.parametrize("author_name", ["Лев Толстой",
                                         "Сергей Довлатов",
                                         "Agatha Christie"])
def test_search_by_author(browser, author_name):
    with allure.step(f"Поиск книг автора: "
                     f" {author_name}"):
        browser.search_by_phrase(author_name)

    with allure.step(f"Книга с названием {author_name} есть в ответе"):
        assert author_name in browser.find_book_authors()


@allure.feature("Тестирование интернет-магазина")
@allure.story("Позитивные тесты.UI")
@allure.severity("blocker")
@allure.title("Добавить книгу в корзину")
@pytest.mark.parametrize("book_name",
                         ["Умная собачка Соня",
                          "Три мушкетера",
                          "Дневник книготорговца"
])
def test_add_to_cart(browser, book_name):
    with allure.step("Поиск книг для добавления"):
        browser.search_by_phrase(book_name)
    with allure.step("Добавить книгу в корзину"):
        browser.click_first_action_button()
    with allure.step("Переход в корзину"):
        browser.go_to_cart()
    with allure.step("Проверить, что корзина не пуста"):
        assert browser.get_cart_item_count() > 0


@allure.feature("Тестирование интернет-магазина")
@allure.story("Негативные тесты.UI")
@allure.severity("major")
@allure.title("Добавить книгу в корзину с невалидным названием")
@pytest.mark.parametrize("book_name", ["$^&*", ";)"])
def test_add_to_cart_negative(browser, book_name):
    with allure.step("Попробовать добавить книгу с невалидным названием"):
        browser.search_by_phrase(book_name)
    with allure.step("Проверить, что ничего не найдено"):
        assert browser.check_empty_result() == "Похоже, у нас такого нет"


@allure.feature("Тестирование интернет-магазина")
@allure.story("Позитивные тесты.UI")
@allure.title("Удаление товара из корзины")
@allure.severity("BLOCKER")
@pytest.mark.parametrize("book_name", ["Умная собачка Соня",
                                       "Дневник книготорговца",
                                       "1984"])
def test_delete_from_cart(browser, book_name):
    with allure.step("Добавить книгу в корзину"):
        browser.search_by_phrase(book_name)
        browser.click_first_action_button()
    with allure.step("Перейти в корзину и удалить книгу"):
        browser.go_to_cart()
        items_before = browser.get_cart_item_count()
        browser.delete_from_cart()
        items_after = browser.get_cart_item_count()
    with allure.step("Проверить, что товар больше не существует в списке"):
        assert items_before < items_after
