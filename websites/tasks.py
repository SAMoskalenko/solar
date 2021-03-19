from datetime import datetime as dt

import requests
from celery import shared_task

from .models import Sites


@shared_task
def checker():
    for site in Sites.objects.all():
        try:
            resp = requests.get(site.url)
            site.is_active = True if resp.status_code == 200 else False
        except:
            site.is_active = False
        site.last_check = dt.now()
        site.save()
