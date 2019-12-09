from rest_framework import serializers
from .models import UploadedDataset


class UploadDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDataset
        fields = "__all__"
