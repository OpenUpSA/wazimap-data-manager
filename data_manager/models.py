# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from wazimap.models import FieldTable


class UploadedDataset(models.Model):
    field_table = models.ForeignKey(FieldTable, on_delete=models.CASCADE)
    dataset_file = models.FileField(upload_to="datasets/")
