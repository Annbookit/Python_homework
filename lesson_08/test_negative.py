import requests

# тестирование негативных запросов

base_url = "https://yougile.com"

token_key = ""
# авторизация в компании с логином и паролем, получение id компании и токена
def test_getting_company_id():
    creds = {
        "login": "", # указать в кавычках нужный логин
        "password": "" # указать в кавычках нужный пароль
    }
    resp = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    company_id = resp.json()["content"][0]["id"]  # получаем id компании

    auth_key = {
        "login": "",
        "password": "",
        "companyId": company_id
    }
    resp = requests.post(base_url + '/api-v2/auth/keys', json=auth_key)
    token = resp.json()["key"] # получаем токен авторизации
    global token_key
    token_key = token
    assert resp.status_code == 201

# добавляем новый проект в выбранную компанию (отправить запрос без обязательного поля)
def test_add_project():
    resp = requests.post(base_url + '/api-v2/projects', headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 400

# изменяем проект, указываем новое название(отправить изменение проекта с пустым названием)
def test_edit():
    project = {
        "title": ""
    }
    id = "f12830e9-b2f8-480a-a3ae-86f072e45a21"
    resp = requests.put(base_url + '/api-v2/projects/' + id, json=project, headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 400

# находим нужный проек по id(отправить запрос без id нужного проекта)
def test_find_id():
    id = ""
    resp = requests.get(base_url + '/api-v2/projects/'+ id, headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 400
