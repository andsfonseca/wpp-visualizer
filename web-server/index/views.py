from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_r(request):
    return HttpResponse("Hello, world. You're at the polls index.")