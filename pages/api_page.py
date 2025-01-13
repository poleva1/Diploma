import requests
import allure


class ApiPage:
    def __init__(self, url: str, my_headers):
        self.url = url
        self.my_headers = my_headers

    @allure.step("Поиск книги в поле Поиск")
    def search_book(self, search_phrase, customer_city):
        my_params = {
            "phrase": search_phrase,
            "customerCityId": customer_city
        }
        response = requests.get(self.url + '/api/v2/search/product', headers=self.my_headers, params=my_params)
        return response

    @allure.step("Добавление книги в корзину")
    def add_book(self, book_id: int):
        payload = {
            "id": book_id
        }
        response= requests.post(self.url+'api/v1/cart/product', headers=self.my_headers, json=payload)
        return response

    @allure.step("Получение кол-ва товаров в корзине")
    def check_cart(self):
        response = requests.get(self.url + '/api/v1/cart/short', headers=self.my_headers)
        return response.json()['data']['quantity']

    @allure.step("Получение id последней добавленной книги в корзине")
    def check_cart_ids(self, num):
        response = requests.get(self.url + '/api/v1/cart', headers=self.my_headers)
        return response.json()['products'][num]['id']

    @allure.step("Удаление книги из корзины")
    def delete_from_cart(self, book_id: int):
        response = requests.delete(self.url + f'/api/v1/cart/product/{book_id}', headers=self.my_headers)
        return response

    @allure.step("Очистка корзины")
    def clean_cart(self):
        response = requests.delete(self.url + '/api/v1/cart', headers=self.my_headers)
        return response
