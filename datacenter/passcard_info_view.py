from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from formatters_time import format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long(),
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
