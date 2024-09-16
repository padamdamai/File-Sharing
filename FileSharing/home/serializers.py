import shutil
import os
from rest_framework import serializers
from .models import Folder, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False)
    )
    folder = serializers.CharField(required=False)

    def zip_files(self, folder_uid):
        # Ensure we are zipping from the correct media folder
        source_folder = os.path.join('media', str(folder_uid))
        zip_destination = os.path.join('public/static/zip', str(folder_uid))

        # Ensure the source folder exists
        if os.path.exists(source_folder):
            shutil.make_archive(zip_destination, 'zip', source_folder)
        else:
            raise serializers.ValidationError(f"Source folder {source_folder} does not exist.")

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []

        for file in files:
            files_obj = File.objects.create(folder=folder, file=file)
            files_objs.append(files_obj)

        # Call the method to zip the folder
        self.zip_files(folder.uid)

        return {'files': {}, 'folder': str(folder.uid)}
