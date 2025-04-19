from rest_framework import serializers
from .models import UserFile

class UserFileSerializer(serializers.ModelSerializer):
    file_url = serializers.FileField(source='stored_file.file', read_only=True)
    size = serializers.IntegerField(source='stored_file.size', read_only=True)

    class Meta:
        model = UserFile
        fields = ['id', 'filename', 'file_type', 'uploaded_at', 'file_url', 'size']
        read_only_fields = ['uploaded_at', 'file_url', 'size']