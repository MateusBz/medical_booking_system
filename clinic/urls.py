from django.urls import path
from .views import VisitCreateView, VisitDetailView, PatientVisitListView, DoctorVisitListView

urlpatterns = [
    path('', VisitCreateView.as_view(), name='visit_creation'),
    path('<int:pk>/', VisitDetailView.as_view(), name='visit_detail'),
    path('visits/patient/', PatientVisitListView.as_view(), name='visits_list'),
    path('visits/doctor/', DoctorVisitListView.as_view(), name='doctor_visits_list'),
    ]