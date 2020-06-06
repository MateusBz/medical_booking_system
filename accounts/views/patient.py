from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView


from ..forms import PatientSignUpForm
from ..models import CustomUser, Patient


class PatientSignUpView(CreateView):
    model = CustomUser
    form_class = PatientSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'accounts/patient_detail.html'
