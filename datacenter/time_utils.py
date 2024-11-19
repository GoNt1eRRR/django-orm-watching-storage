from django.utils.timezone import localtime


def get_duration(entered_at, leaved_at=None):
    entered_time = localtime(entered_at)
    if leaved_at:
        leaved_time = localtime(leaved_at)
        duration = leaved_time - entered_time
    else:
        current_time = localtime()
        duration = current_time - entered_time
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f'{hours}:{minutes}'


def is_visit_long(duration, minutes=60):
    return duration.total_seconds() > minutes * 60
