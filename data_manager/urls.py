from django.urls import path

from .views import UploadDatasetView

urlpatterns = [path("", UploadDatasetView.as_view(), name="api_upload")]
