from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.shortcuts import redirect
from ..models import Visit
from ..forms import VisitCreateForm


class VisitCreateView(LoginRequiredMixin, CreateView):
    model = Visit
    form_class = VisitCreateForm
    template_name = 'clinic/visit_creation.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.patient = self.request.user
        form.instance.doctor.occupied = True
        form.instance.doctor.save()
        return super().form_valid(form)


class PatientVisitListView(LoginRequiredMixin, ListView):
    model = Visit
    context_object_name = 'visits'
    template_name = 'clinic/visit_list.html'
    login_url = 'login'

    def get_queryset(self, *args, **kwargs):
        qs = super(PatientVisitListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(patient=self.request.user)
        return qs


class VisitDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = 'clinic/visit_detail.html'