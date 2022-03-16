from django.urls import path
from .views import ProjectListView, ProjectCreateView
from . import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', ProjectListView.as_view(), name='home'),
    path('project/new/', ProjectCreateView.as_view(), name='new-project'),
]