from datacenter.models import Visit
from django.shortcuts import render
from .services import get_passcard_visit_info


def get_non_closed_visits():
    active_visitors = Visit.objects.filter(leaved_at=None)
    return [get_passcard_visit_info(visit) for visit in active_visitors]


def storage_information_view(request):
    non_closed_visits = get_non_closed_visits()
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
