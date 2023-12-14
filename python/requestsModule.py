from requests_oauthlib import OAuth2Session
from requests import get, post, put, delete


client_id = "fbb376be8e5a4067bd67eda8150576f8"
client_secret = "476cef73eb9c48759b23cb1091c3e467"
auth_url = "https://oauth.yandex.ru/authorize"
token_url = "https://oauth.yandex.ru/token"
oauth = OAuth2Session(client_id=client_id)
authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
code = input("Вставьте одноразовый код: ")
token = oauth.fetch_token(token_url=token_url,
                          code=code,
                          client_secret=client_secret)
access_token = token["access_token"]
print(access_token)

headers = {"Authorization": f"OAuth {access_token}"}
r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
print(r.json())

#
# from requests import get, ConnectionError
#
# params = {"ll": "37.677751,55.757718",
#           "spn": "0.9,0.9",
#           "l": "map"}
# try:
#     response = get("https://static-maps.yandex.ru/1.x/", params=params)
# except ConnectionError:
#     print("Проверьте подключение к сети.")
# else:
#     with open("map2.png", "wb") as file:
#         file.write(response.content)
