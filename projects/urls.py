from django.urls import path, include
from .views import (ProjectListView,
                    ProjectCreateView,
                    ProfileViewSet,
                    ProjectViewSet
                )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('home/', ProjectListView.as_view(), name='home'),
    path('project/new/', ProjectCreateView.as_view(), name='new-project'),
    path('api/', include(router.urls)),
]