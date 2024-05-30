# myapp/views.py
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import DataTS
from .tables import DataTSTable

def data_ts_list(request):
    table = DataTSTable(DataTS.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'myapp/data_ts_list.html', {'table': table})