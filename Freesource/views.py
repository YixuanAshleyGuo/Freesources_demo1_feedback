from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
#import json

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ev.*,t.tag_name,ex.expire_type FROM Events ev INNER JOIN Events e ON ev.event_id = e.event_id INNER JOIN Tag t ON ev.tag_id = t.tag_id INNER JOIN ExpirationType ex ON ev.expire_type_id = ex.expire_type_id")
        events = dictfetchall(cursor)
        #events_json = json.dumps(events)
    context = {
        'events': events,
    }
    return render(request,'Freesource/index.html', context)

# transfer the raw pulled database data into dictionary format
def dictfetchall(cursor):
#    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]