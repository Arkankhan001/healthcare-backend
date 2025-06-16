from rest_framework import viewsets, generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, Doctor, PatientDoctorMapping, User
from .serializers import *

# Register user view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Patient CRUD API
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Doctor CRUD API
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Patient-Doctor mapping API
class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        if patient_id:
            return self.queryset.filter(patient__id=patient_id)
        return self.queryset
