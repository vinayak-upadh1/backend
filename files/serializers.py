from rest_framework import serializers
from .models import UserFile

class UserFileSerializer(serializers.ModelSerializer):
    file_url = serializers.FileField(source='stored_file.file', read_only=True)
    size = serializers.IntegerField(source='stored_file.size', read_only=True)

    class Meta:
        model = UserFile
        fields = ['id', 'original_filename', 'file_type', 'uploaded_at', 'file_url', 'size']
        read_only_fields = ['uploaded_at', 'file_url', 'size']

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.method == 'POST':
            file_obj = request.FILES.get('file')
            if file_obj and file_obj.size > 10 * 1024 * 1024:  # 10 MB
                raise serializers.ValidationError("File size must not exceed 10MB.")
        return attrs