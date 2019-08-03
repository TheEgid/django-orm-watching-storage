from datacenter.models import Passcard
from django.shortcuts import get_object_or_404
from django.utils import timezone


def format_duration(duration):
    _duration = str(duration)
    if len(_duration) > 8:
        return _duration[:-7]
    return _duration


def is_visit_long(duration, minutes=60):
    seconds_in_minute = 60
    return duration.total_seconds() >= seconds_in_minute * minutes


def get_passcard_visit_info(_visit):
    if _visit.leaved_at:
        duration = _visit.leaved_at - _visit.entered_at
    else:
        duration = (timezone.now() - _visit.entered_at)
    _passcard = get_object_or_404(Passcard, id=_visit.passcard_id)
    return {
        "who_entered": _passcard.owner_name,
        "entered_at": _visit.entered_at,
        "duration": format_duration(duration),
        "is_strange": is_visit_long(duration)
    }
