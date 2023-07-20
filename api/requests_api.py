import requests

status = "available"
url = "https://petstore.swagger.io/v2/user"
name = "Lol12345"
name2 = "Lol67890"
id = 2462275
headers = {"accept": "application/json"}


def PrintRes(res):
    if "application/json" in res.headers:
        print(res.json())
    else:
        print(res.text)
    print(res.status_code)


# -----------------------------------------------------
print("Проверка POST(user)")
res = requests.post(
    f"{url}",
    json={
        "id": id,
        "username": name,
        "firstName": "test",
        "lastName": "test",
        "email": "test",
        "password": "test",
        "phone": "test",
        "userStatus": 0,
    },
    headers=headers,
)
PrintRes(res)
# -----------------------------------------------------
print("Проверка GET(user)")
res = requests.get(
    f"{url}/login?username={name}&password=test",
    headers=headers,
)
PrintRes(res)
# -----------------------------------------------------
print("Проверка PUT(user)")
res = requests.put(
    f"{url}/{name}",
    json={
        "id": id,
        "username": name,
        "firstName": "Lol67890",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0,
    },
    headers=headers,
)
PrintRes(res)
# -----------------------------------------------------
print("Проверка Delete(user)")
res = requests.delete(
    f"{url}/{name}",
    headers=headers,
)
PrintRes(res)