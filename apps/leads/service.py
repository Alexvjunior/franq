from apps.leads.models import Lead
from common.pipedriver import Pipedriver
from common.rd_station import RDStation


class LeadService:
    rd_station = RDStation()
    pipedriver = Pipedriver()

    def send_lead_to_rd_station(
        self,
        name: str,
        email: str,
        phone: str,
        interest: str,
    ) -> str:
        try:
            return self.rd_station.send_lead(name, email, phone, interest)
        except Exception as e:
            print(e)
            return None

    def send_lead_to_pipedriver(
        self,
        name: str,
        email: str,
        phone: str,
        interest: str,
        rd_station_id: str
    ) -> str:
        try:
            return self.pipedriver.send_lead(
                name, email, phone, interest, rd_station_id
            )
        except Exception as e:
            print(e)
            return None

    def create_leads_local(self, name, email, phone, interest):
        Lead.objects.create(name=name, email=email,
                            phone=phone, interest=interest)
