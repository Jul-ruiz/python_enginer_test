from django.urls import path
from .views import MedicalImageResultListCreate, MedicalImageResultRetrieveUpdateDestroy

urlpatterns = [
    path('api/elements/', MedicalImageResultListCreate.as_view(), name='element-list-create'),
    path('api/elements/<str:pk>/', MedicalImageResultRetrieveUpdateDestroy.as_view(), name='element-detail'),
]
