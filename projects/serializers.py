from rest_framework import serializers
from users.models import Profile
from .models import Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image','user_bio','user_contact']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','image','description']