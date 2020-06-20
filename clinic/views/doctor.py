from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import redirect, get_list_or_404
from django.http import Http404
from ..models import Visit, DoctorSchedule
from ..forms import VisitCreateForm, DoctorScheduleCreateForm


class DoctorVisitListView(LoginRequiredMixin, ListView):
    model = Visit
    context_object_name = 'visits'
    template_name = 'clinic/visit_list.html'
    login_url = 'login'

    def get_queryset(self, *args, **kwargs):
        qs = super(DoctorVisitListView, self).get_queryset(*args, **kwargs)
        try:
            doctor = DoctorSchedule.objects.filter(doctor=self.request.user.id)[:1]
        except DoctorSchedule.DoesNotExist:
            raise Http404('Brak danych')
        qs = qs.filter(doctor=doctor)
        return qs


class DoctorScheduleListView(ListView):
    model = DoctorSchedule
    template_name = 'clinic/doctor_schedule.html'
    context_object_name = 'free_dates'

    def get_queryset(self, *args, **kwargs):
        qs = super(DoctorScheduleListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(occupied=False)
        return qs


class DoctorScheduleDetailView(DetailView):
    model = DoctorSchedule
    template_name = 'clinic/doctor_schedule_detail.html'
    

class DoctorScheduleCreateView(LoginRequiredMixin, CreateView):
    model = DoctorSchedule
    form_class = DoctorScheduleCreateForm
    template_name = 'clinic/doctor_schedule_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.doctor = self.request.user.doctor
        form.instance.date.occupied = True
        form.instance.time.occupied = True
        form.instance.date.save()
        form.instance.time.save()
        return super().form_valid(form)