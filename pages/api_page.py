from pickle import APPEND
import requests
import allure

ApiPage = "https://web-gate.chitai-gorod.ru/"
access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMzc0MDQ5LCJpYXQiOjE3MzYzMzQ1MjIsImV4cCI6MTczNjMzODEyMiwidHlwZSI6MjB9.b4Zwm2yxE1trGNtFunDbaAJ3PeBwxRbfI6hMJ8Xynoo"
my_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
    'Cookie': '__ddg1_=xkIEIxEwaq1iHDXvOTl9; __ddg2_=bpH1A25mPTZ8OGUx; __ddg9_=188.166.83.219; __ddg8_=AQrjExi08IZ4kjhs; __ddg10_=1736327150'
}

class ApiPage:
    def __init__(self, url: str, access_token: str):
        self.url = url
        self.access_token = access_token

    @allure.step("Поиск книги в поле Поиск")
    def search_book(self, payload):
        payload = {
            "book_title": title,
            "authors_lastName": author_lastName
        }
        response = requests.get(self.url+'/api/v1/search/product', headers=my_headers, json=payload)
        return response

    @allure.step("Добавление книги в корзину")
    def add_book(self, book_id: int):
        payload = {
            "id": book_id
        }
        response= requests.post(self.url+'api/v1/cart/product', headers=my_headers, json=payload)
        return response

    @allure.step("Получение кол-ва товаров в корзине")
    def check_cart(self):
        response = requests.get(self.url+'/api/v1/cart/short', headers=my_headers)
        print(response)
        return response.json()['data']['quantity']

    @allure.step("Удаление книги из корзины")
    def delete_from_cart(self, book_id: int):
        response = requests.delete(self.url+'/api/v1/cart/product/181959352', headers=my_headers)
        print(response)

    @allure.step("Добавление товара в корзину с несуществующим id")