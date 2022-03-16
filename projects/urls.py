from django.urls import path
from .views import ProjectCreateView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('project/new/', ProjectCreateView.as_view(), name='new-project'),
]