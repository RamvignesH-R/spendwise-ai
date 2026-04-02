import urllib.request
import urllib.parse
import json

data = urllib.parse.urlencode({'username': 'admin@spendwise.com', 'password': 'admin'}).encode('ascii')
req = urllib.request.Request("http://15.206.178.181:8000/auth/login", data=data)
try:
    with urllib.request.urlopen(req) as response:
        print("SUCCESS:", response.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTP ERROR {e.code}:", e.read().decode())
except Exception as e:
    print("FATAL ERROR:", getattr(e, 'read', lambda: str(e))())
