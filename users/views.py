from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})