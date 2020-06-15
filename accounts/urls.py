from django.urls import path

from .views import index, patient, doctor

urlpatterns = [
    path('', index.IndexView.as_view(), name='index'),
    path('patient/<int:pk>', patient.PatientDetailView.as_view(), name='patient_detail'),
    path('doctor/<int:pk>', doctor.DoctorDetailView.as_view(), name='doctor_detail'),
]
