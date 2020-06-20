from django.urls import path
from .views import patient, doctor

urlpatterns = [
    path('', patient.VisitCreateView.as_view(), name='visit_creation'),
    path('doctors/', doctor.DoctorScheduleListView.as_view(), name='doctor_visit_list_accessible'),
    path('doctors/schedule_create/', doctor.DoctorScheduleCreateView.as_view(), name='doctor_schedule_create'),
    path('doctors/<int:pk>/', doctor.DoctorScheduleDetailView.as_view(), name='doctor_schedule_detail'),
    path('visits/patient/<int:pk>/delete/', patient.VisitDelete.as_view(), name='visit_delete'),
    path('visits/patient/<int:pk>', patient.VisitDetailView.as_view(), name='visit_detail'),
    path('visits/patient/', patient.PatientVisitListView.as_view(), name='visits_list'),
    path('visits/doctor/', doctor.DoctorVisitListView.as_view(), name='doctor_visits_list'),
    ]
