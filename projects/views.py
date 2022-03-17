from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from rest_framework import viewsets, permissions
from users.models import Profile
from .models import Project, Review
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


class ProjectDetailView(DetailView):
    model = Project




class UserProjectListView(ListView):
    model = Project # blog/post_list.html requires this template to run
    template_name = 'blog/user_projects.html' # Or specify the template to use here
    context_object_name = 'project'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_posted')




# Search method
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		projects = Project.objects.filter(author__username__contains=searched)
	
		return render(request, 'projects/search.html', {'projects':projects})
	else:
		return render(request, 'projects/search.html')




def review_rating(request):
    if request.method == 'GET':
        proj_id = request.GET.get('proj_id')
        project = Project.objects.get(id=proj_id)
        comment = request.GET.get('comment')
        design_rate = request.GET.get('design_rate')
        content_rate = request.GET.get('content_rate')
        usability_rate = request.GET.get('usability_rate')
        user = request.user

        review = Review(user=user, project=project, comment=comment, design_rate=design_rate, content_rate=content_rate, usability_rate=usability_rate)
        review.save()
        return redirect('home')


# API Views
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
