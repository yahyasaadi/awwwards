from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from rest_framework import viewsets, permissions
from users.models import Profile
from .models import Project
from .serializers import ProfileSerializer, ProjectSerializer

# Create your views here.
def home(request):
    return render(request, 'projects/base.html')


class ProjectListView(ListView):
    model = Project
    ordering = ['-date_posted']

# Post a project
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project 
    fields = ['title', 'image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# API Views
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]