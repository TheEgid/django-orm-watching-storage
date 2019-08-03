from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .services import get_passcard_visit_info


def passcard_info_view(request, passcode):
    _passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.order_by("-created_at"). \
        filter(passcard_id=_passcard.id)
    this_passcard_visits = [get_passcard_visit_info(visit) for
                            visit in all_visits]
    context = {
        "passcard": _passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
