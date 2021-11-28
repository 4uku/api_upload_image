from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ImageUploadSerializer


class ImageUploadViewSet(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        images = dict(request.data)['image']
        arr = []
        for img in images:
            dict_img = {}
            dict_img['image'] = img
            img_serializer = ImageUploadSerializer(data=dict_img)
            img_serializer.is_valid(raise_exception=True)
            img_serializer.save()
            arr.append(img_serializer.data)
        return Response(arr, status=status.HTTP_201_CREATED)
