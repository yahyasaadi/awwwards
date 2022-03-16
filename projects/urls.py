from django.urls import path, include
from .views import (ProjectListView,
                    ProjectCreateView,
                    ProjectDetailView,
                    UserProjectListView,
                    ProfileViewSet,
                    ProjectViewSet
                )
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', ProjectListView.as_view(), name='home'),
    path('project/new/', ProjectCreateView.as_view(), name='new-project'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('user/<str:username>', UserProjectListView.as_view(), name='user-projects'),
    path('search/', views.search, name='search'),
    path('api/', include(router.urls)),
]