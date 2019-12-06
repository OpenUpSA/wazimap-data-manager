import logging
import psycopg2
from django.conf import settings
from .models import UploadedDataset

log = logging.getLogger(__name__)


class UploadedDataSet(object):
    """
    Class to create and process datasets that were uploaded from the admin site.
    """

    def __init__(self, dataset):
        self._dataset = dataset

    def insert_data(self):
        """
        Insert data from the uploaded file into the table corresponding to the 
        FieldTable. We assume the file is in the correct format and contains 
        valid values.
        """
        connection = psycopg2.connect(settings.DATABASE_URL)
        cursor = connection.cursor()

        table_name = self._dataset.field_table.name.lower()

        cursor.copy_from(self._dataset.dataset_file, table_name, sep=",")

        connection.commit()


def handle_uploaded_dataset(upload_file_id):
    """
    Lets get the uploaded file and upload the data to postgresql
    """
    dataset = UploadedDataset.objects.get(id=upload_file_id)
    uploaded_dataset = UploadedDataSet(dataset)
    uploaded_dataset.insert_data()
