import configuration
import requests
import data


def get_docs():
    # https://087dee31-ebc5-40c1-b846-2330a6139f44.serverhub.praktikum-services.ru/docs/
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_logs():
    # https://087dee31-ebc5-40c1-b846-2330a6139f44.serverhub.praktikum-services.ru/api/logs/main/
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


def users_table():
    # https://087dee31-ebc5-40c1-b846-2330a6139f44.serverhub.praktikum-services.ru/api/db/resources/user_model.csv
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # подставляем полный url
                         json=product_ids,  # тут тело
                         headers=data.headers)  # а здесь заголовки

