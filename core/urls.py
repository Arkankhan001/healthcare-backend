from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('', include(router.urls)),
]
