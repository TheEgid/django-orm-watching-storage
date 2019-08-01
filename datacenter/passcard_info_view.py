from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .services import get_passcard_visit_info


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    all_visits = Visit.objects.filter(passcard_id=passcard.id)
    this_passcard_visits = [get_passcard_visit_info(visit) for
                            visit in all_visits]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
