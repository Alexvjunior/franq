from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.leads.service import LeadService
from apps.leads.forms import LeadForm

_service = LeadService()


@csrf_exempt
def capture_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        interest = form.cleaned_data['interest']

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

    form = LeadForm()
    context = {
        'form': form,
    }

    return render(request, "capture.html", context)
