import requests
from django.conf import settings


class RDStation:
    _headers = None
    _url_lead = None

    def __init__(self) -> None:
        self._url_lead = f"{settings.RDSTATION_API_URL}/platform/contacts"

    def _setup(self) -> None:
        if self._headers is None:
            url = f"{settings.RDSTATION_API_URL}/auth/token"

            payload = {
                "client_id": settings.RDSTATION_CLIENT_ID,
                "client_secret": settings.RDSTATION_CLIENT_SECRET,
                "code": 200,
            }
            headers = {"accept": "application/json", "content-type": "application/json"}

            response = requests.post(url, json=payload, headers=headers)
            self._headers = {
                "Content-Type": "application/json",
                "Authorization": f'Bearer {response.json()["access_token"]}',
            }

    def send_lead(self, name, email, phone, interest):
        self._setup()
        payload = {
            "name": name,
            "email": email,
            "mobile_phone": phone,
            "tags": [interest],
        }

        response = requests.post(self._url_lead, json=payload, headers=self._headers)

        if response.status_code != 200:
            print(
                "Erro ao enviar o lead para o RD Station. Status code:",
                response.status_code,
            )
            return

        return response.json()["uuid"]
