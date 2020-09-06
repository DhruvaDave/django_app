from django.shortcuts import render

# Create your views here.
# Django
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Loal Django Apps
from .models import Student


class AboutusTemplate(TemplateView):
    template_name = 'aboutus.html'

    def get_context_data(self, *a, **args):
        context = super(AboutusTemplate, self).get_context_data(*a, **args)
        context['title'] = 'About Us Page'

        return context


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        students = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(students, self.paginate_by)
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)
        context['students'] = students
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


# @method_decorator(login_required, name='dispatch')
class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student_create.html'

    # fields = 'all'
    fields = ('name', 'email', 'age', 'semester', 'enroll_num', 'gender')
    success_url = reverse_lazy('student_list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student_update.html'
    context_object_name = 'student'
    # permission_required = ('student.2_student_can_do_all_crud_permission')
    fields = ('name', 'email', 'age', 'semester', 'gender')

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.enroll_num})


class StudentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'student_delete.html'
    context_object_name = 'student'
    success_message = "%(name)s is Delete"
    success_url=reverse_lazy('student_list')
    # def get_success_url(self):
    #     return reverse_lazy('student_list')
