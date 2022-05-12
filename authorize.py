from dotenv import load_dotenv
import os
import requests
import base64

load_dotenv()

class Authorize():
    def __init__(self) -> None:
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")
        self.target_url = os.getenv("AUTH_URL")
        pass

    def auth(self):
        auth_str = f'{self.consumer_key}:{self.consumer_secret}'

        sample_string_bytes = auth_str.encode("ascii")
        
        base64_bytes = base64.b64encode(sample_string_bytes)

        base64_string = base64_bytes.decode("ascii")

        print(base64_string)
        
        header = {
            'Authorization': f'Bearer {base64_string}'
        }

        body_str = "grant_type=client_credentials"
    
        print(self.target_url + body_str)

        response = requests.request("GET", self.target_url + body_str, headers = header)

        if response.status_code == 200:
            return response.json()
        else:
            print(response)


