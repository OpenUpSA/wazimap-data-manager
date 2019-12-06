# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.messages import api as messages_api
from django.contrib.admin.views.decorators import staff_member_required
from django_q.tasks import async_task

from .dataset_upload import handle_uploaded_dataset
from .forms import UploadedDatasetForm

log = logging.getLogger(__name__)


@staff_member_required
def add_dataset(request):
    if request.method == "POST":
        form = UploadedDatasetForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                dataset = form.save()
                task_id = async_task(
                    "data_manager.dataset_upload.handle_uploaded_dataset", dataset.id
                )
                messages_api.success(
                    request, "Dataset has been upload and is currently being processed"
                )
                return HttpResponseRedirect("/admin/")
            except Exception as e:
                log.debug(e)
                messages_api.error(
                    request, "Error occurred while uploading dataset: {}".format(e)
                )
    else:
        form = UploadedDatasetForm
    return render(
        request,
        "data_manager/dataset_form.html",
        {"model_name": "Field table", "form": form},
    )
