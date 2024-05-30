# myapp/urls.py
from django.urls import path
from .views import data_ts_list

urlpatterns = [
    path('datats/', data_ts_list, name='datats_list'),
    # other url patterns...
]

