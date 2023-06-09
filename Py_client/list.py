import requests

end_point = "http://127.0.0.1:8000/auth/"

auth_response = requests.post(end_point,json={"username":"vijay","password":"saradhi123"})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    end_point = "http://127.0.0.1:8000/api/books/"

    get_response = requests.get(end_point,headers=headers)
    print(get_response.json())

