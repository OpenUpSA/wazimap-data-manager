from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework import status
from django_q.tasks import async_task

from .models import UploadedDataset
from .serializer import UploadDatasetSerializer


class UploadDatasetView(APIView):
    """
    Upload properly formatted dataset to wazimap
    """

    parser_classes = (MultiPartParser,)

    def get(self, request):
        """
        Show all the dataset that have been uploaded
        """
        query = UploadedDataset.objects.all()
        serializer = UploadDatasetSerializer(query, many=True)

        return Response({"results": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UploadDatasetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            dataset = serializer.save()
            task_id = async_task(
                "data_manager.dataset_upload.handle_uploaded_dataset", dataset.id
            )
            return Response(
                {
                    "success": "Dataset has being uploaded and is currently being processed "
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
