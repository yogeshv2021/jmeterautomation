import requests

class Hybrid:
    def __init__(self):
        self.token=None

    def login_via_api(self,BaseURL,username,password):
        response = requests.post(f"{BaseURL}/portal/login",json={"username": username, "password":password})
        if response.status_code !=200:
            raise Exception("login failed for the given credentials")

        self.token=response.json().get("access_token")
        if not self.token:
            raise Exception("token is not present")

        print(f"token saved.token is {self.token}")
