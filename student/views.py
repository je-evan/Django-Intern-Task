from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    ListView
)

from django.urls import reverse_lazy
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    paginate_by = 3

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/update.html'
    context_object_name = 'student'
    fields = [
        'name',
        'age',
        'address',
        'grade',
        'major',
    ]

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/create.html'
    fields = [
        'name',
        'age',
        'address',
        'grade',
        'major',
    ]
    success_url = reverse_lazy('list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/delete.html'
    success_url = reverse_lazy('list')

