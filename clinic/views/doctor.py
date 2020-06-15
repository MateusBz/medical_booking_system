from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import redirect
from ..models import Visit, DoctorSchedule
from ..forms import VisitCreateForm


class DoctorVisitListView(LoginRequiredMixin, ListView):
    model = Visit
    context_object_name = 'visits'
    template_name = 'clinic/visit_list.html'
    login_url = 'login'

    def get_queryset(self, *args, **kwargs):
        qs = super(DoctorVisitListView, self).get_queryset(*args, **kwargs)
        doctor = DoctorSchedule.objects.get(doctor=self.request.user.id)
        qs = qs.filter(doctor=doctor)
        return qs


class DoctorScheduleListView(ListView):
    model = DoctorSchedule
    template_name = 'clinic/doctor_schedule.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(DoctorScheduleListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(occupied =False)
        return qs