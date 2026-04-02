import requests

res = requests.post(
    "http://15.206.178.181:8000/auth/login",
    data={"username": "test2@spendwise.com", "password": "admin"}
)
print("STATUS CODE:", res.status_code)
print("RESPONSE:", res.text)
