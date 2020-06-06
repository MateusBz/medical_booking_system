from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView


from ..forms import DoctorSignUpForm
from ..models import CustomUser, Doctor


class DoctorSignUpView(CreateView):
    model = CustomUser
    form_class = DoctorSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class DoctorDetailView(DetailView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'accounts/doctor_detail.html'
