# myapp/tables.py
import django_tables2 as tables
from .models import DataTS

class DataTSTable(tables.Table):
    class Meta:
        model = DataTS
        template_name = "django_tables2/bootstrap.html"  # Use the bootstrap template for the table
        fields = ('data_static', 'index_symbol', 'weight', 'date', 'price')  # fields to display
