from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'projects/base.html')


# Post a project
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project 
    fields = ['title', 'image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)