import requests
import logging
import base64
import os
from dotenv import load_dotenv

load_dotenv()


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AtlassianAPIHandler():
    def __init__(self):
        self.email = os.getenv('EMAIL')
        self.account_number = os.getenv('ACCOUNT_NUMBER')
        self.api_token = os.getenv('API_TOKEN')
        self.base_url = os.getenv('BASE_URL')
        self.auth_string = self._gen_auth_string()
    
    def test_connection(self):
        response = self._call_base_api()
        if response.status_code == 200:
            return ("Successful connection")
        return("Connection Failed.")
    
    def _call_base_api(self):
        if self.base_url[-1] == "/":
            new_base = self.base_url[::-1]
            self.base_url = new_base

        route = "/rest/api/content/"
        url = f"https://{self.base_url}{route}"
        payload = {}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.auth_string}",
        }
        logger.debug(f"Basic {self.auth_string}")
        response = requests.request("GET", url, headers=headers, data=payload)
        logger.debug(response.status_code)
        return response


    def _gen_auth_string(self):
        logger.debug(f"Generating authstring from {self.email}:{self.api_token}")
        auth_string = base64.b64encode(bytes(f"{self.email}:{self.api_token}", "utf-8")).decode()
        logger.debug(f"Auth string generated: {auth_string}")
        return auth_string

def main():
    handler = AtlassianAPIHandler()
    print(handler.test_connection())

if __name__ == "__main__":
    main()
