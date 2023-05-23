import requests
from django.conf import settings


class Pipedriver:
    _headers = None
    _url_lead = None

    def __init__(self) -> None:
        self._url_lead = f"{settings.PIPEDRIVE_API_URL}/deals"

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
            if response.status_code != 200:
                return

            self._headers = {
                "Content-Type": "application/json",
                "Authorization": f'Bearer {response.json()["access_token"]}',
            }

    def send_lead(self, name, email, phone, interest, rd_station_id):
        self._setup()
        payload = {
            "title": f"{name}-{email}-{phone}",
            "owner_id": rd_station_id,
            "value": {
                "name": name,
                "email": email,
                "phone": phone,
                "interest": interest,
            },
        }

        response = requests.post(self._url_lead, json=payload, headers=self._headers)

        if response.status_code != 200:
            print(
                "Erro ao enviar o lead para o Pipedriver. Status code:",
                response.status_code,
            )
            return

        return response.json()["data"]
