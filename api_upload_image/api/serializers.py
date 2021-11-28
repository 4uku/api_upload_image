import os

from rest_framework.serializers import ModelSerializer, ValidationError

from .models import ImageUpload


class ImageUploadSerializer(ModelSerializer):

    class Meta:
        model = ImageUpload
        fields = ('image',)

    def validate_image(self, value):
        current_files = os.listdir('media/images/')
        max_size = 200000
        if str(value) in current_files:
            raise ValidationError(
                'изображение с таким именем уже было загружено')
        if value.size > max_size:
            raise ValidationError(
                'изображение превышает допустимый размер в 200 кб'
            )
        return value
