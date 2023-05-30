from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def introduce(request):
    return render(request, 'introduction.html', {'name': 'Minh Ngo', 'job': 'Software Developer', 'school': 'Vietnamese-German University', 'language': {'first': 'Vietnamese', 'second': 'English', 'third': 'German'}})