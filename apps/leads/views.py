from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.leads.service import LeadService

_service = LeadService()


@csrf_exempt
def capture_lead(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        interest = request.POST.get("interest")

        rdstation_uuid = _service.send_lead_to_rd_station(
            name,
            email,
            phone,
            interest
        )

        if rdstation_uuid:
            pipedrive_response = _service.send_lead_to_pipedriver(
                name, email, phone, interest, rdstation_uuid
            )

            if pipedrive_response.status_code == 201:
                messages.success(request, "Formulário enviado com sucesso!")
        else:
            messages.success(
                request,
                "Formulário enviado com algumas pendências de integração!"
            )

        _service.create_leads_local(name, email, phone, interest)

    return render(request, "capture.html")
