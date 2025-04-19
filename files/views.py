from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.response import Response

from .filters import UserFileFilter
from .models import StoredFile, UserFile
from .serializers import UserFileSerializer
from .utils import UserFileUtil


class UserFileCreateView(generics.CreateAPIView):
    queryset = UserFile.objects.all()
    serializer_class = UserFileSerializer

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file")
        if not file_obj:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        file_hash = UserFileUtil.compute_file_hash(file_obj)

        stored_file, created = StoredFile.objects.get_or_create(
            file_hash=file_hash, defaults={"file": file_obj, "size": file_obj.size}
        )

        user_file = UserFile.objects.create(
            stored_file=stored_file,
            original_filename=file_obj.name,
            file_type=file_obj.content_type,
        )

        serializer = self.get_serializer(user_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserFileListView(generics.ListAPIView):
    queryset = UserFile.objects.select_related("stored_file").all()
    serializer_class = UserFileSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = UserFileFilter
    search_fields = ["original_filename"]
    ordering_fields = ["uploaded_at", "original_filename", "stored_file__size"]
    ordering = ["-uploaded_at"]


class UserFileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserFile.objects.select_related("stored_file").all()
    serializer_class = UserFileSerializer


class UserFileDeleteView(generics.DestroyAPIView):
    queryset = UserFile.objects.select_related("stored_file").all()
    serializer_class = UserFileSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        stored_file = instance.stored_file

        self.perform_destroy(instance)

        if not stored_file.user_files.exists():
            stored_file.file.delete(save=False)  # delete file from disk
            stored_file.delete()
        return Response(
            {"message": "File deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
