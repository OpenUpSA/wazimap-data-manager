# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UploadedDataset
from django_q.tasks import async_task
from django.contrib import messages


class UploadDatasetAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        messages.add_message(
            request, messages.INFO, "Dataset is currently being processed."
        )
        super().save_model(request, obj, form, change)
        task_id = async_task(
            "data_manager.dataset_upload.handle_uploaded_dataset", obj.id
        )


admin.site.register(UploadedDataset, UploadDatasetAdmin)
