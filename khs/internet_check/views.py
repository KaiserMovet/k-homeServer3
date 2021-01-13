from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import InternetSpeed, InternetStatus
# Main


def index(request):
    template = loader.get_template('internet_check/base.html')
    return HttpResponse(template.render())


# API


def api_internet_speed(_):
    internet_speed = serializers.serialize(
        "json", InternetSpeed.objects.order_by('-date'))
    return HttpResponse(internet_speed)


def api_internet_status(_):
    internet_status = serializers.serialize(
        "json", InternetStatus.objects.order_by('-change_time'))
    return HttpResponse(internet_status)
