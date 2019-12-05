from django import forms
from wazimap.models import FieldTable
from django.contrib.admin import widgets


class DataUploadForm(forms.Form):
    field_tables = FieldTable.objects.all()
    field_table = forms.ModelChoiceField(field_tables)
    data_file = forms.FileField(widget=widgets.AdminFileWidget)
