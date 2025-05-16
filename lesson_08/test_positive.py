import requests

# тестирование позитивных запросов

base_url = "https://yougile.com"

token_key = ""
# авторизация в компании с логином и паролем, получение id компании и токена
def test_getting_company_id():
    creds = {
        "login": "sebast57945@gmail.com", # указать в кавычках нужный логин
        "password": "Qa15052024" # указать в кавычках нужный пароль
    }
    resp = requests.post(base_url + '/api-v2/auth/companies', json=creds)
    company_id = resp.json()["content"][0]["id"]  # получаем id компании

    auth_key = {
        "login": "sebast57945@gmail.com",
        "password": "Qa15052024",
        "companyId": company_id
    }
    resp = requests.post(base_url + '/api-v2/auth/keys', json=auth_key)
    token = resp.json()["key"] # получаем токен авторизации
    global token_key
    token_key = token
    assert resp.status_code == 201

# добавляем новый проект в выбранную компанию
def test_add_project(title = 'Новый проект'):
    project = {
        "title": title
    }
    resp = requests.post(base_url + '/api-v2/projects', json=project, headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 201

# изменяем проект, указываем новое название
def test_edit():
    project = {
        "title": "new project"
    }
    id = "f12830e9-b2f8-480a-a3ae-86f072e45a21"
    resp = requests.put(base_url + '/api-v2/projects/' + id, json=project, headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 200

# находим нужный проек по id
def test_find_id():
    id = "b843cb63-d996-4391-b0c6-0fdec07821dc"
    resp = requests.get(base_url + '/api-v2/projects/'+ id, headers={'Authorization': f'Bearer {token_key}'})
    assert resp.status_code == 200
