from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_utils import get_duration, format_duration
from django.utils.timezone import localtime


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in active_visits:
        entered_at = visit.entered_at
        duration = get_duration(entered_at)
        formatted_duration = format_duration(duration)
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(entered_at).strftime("%d-%m-%Y %H:%M:%S"),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
