from django import forms

# from wazimap.models import FieldTable
# from django.contrib.admin import widgets
from .models import UploadedDataset


class UploadedDatasetForm(forms.ModelForm):
    class Meta:
        model = UploadedDataset
        fields = "__all__"
