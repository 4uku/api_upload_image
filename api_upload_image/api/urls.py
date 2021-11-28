from django.urls import path

from .views import ImageUploadViewSet

urlpatterns = [
    path('image/', ImageUploadViewSet.as_view(), name='upload_image'),
]
