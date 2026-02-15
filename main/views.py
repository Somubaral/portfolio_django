# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Skill, Project

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
    })