import requests
import allure

from Diploma.Diploma.pages.api_page import ApiPage
from settings import access_token
url = "https://web-gate.chitai-gorod.ru/"
api = ApiPage(url, access_token)

@allure.step("Поиск книги по названию. API")
def test_search_by_title():
    title = "Книготорговец"
    resp_search = api.search_book(title)
    assert resp_search.status_code == 200
    assert title in resp_search.text

@allure.step("Поиск книги по фамилии автора. API")
def test_search_by_author():
    author_lastName = "Байтелл"
    resp_search = api.search_book(author_lastName)
    assert resp_search.status_code == 200
    assert author_lastName in resp_search.text

@allure.step("Добавление книги в корзину. API")
def test_add_book():
    book_id = 2648551
    books_before = api.check_cart()
    print(books_before)
    resp_add = api.add_book(book_id)
    assert resp_add.status_code == 200

@allure.step("Получение кол-ва товаров в корзине. API")
def test_check_cart():

@allure.step("Удаление книги из корзины.API")
def test_delete_from_cart():
    book_id = 181959352
    resp_delete = api.delete_from_cart(book_id)
    assert resp_delete.status_code == 204