from django.http import HttpResponse
from django.shortcuts import render
#import collections
import operator

def home(request):
    return render(request, "home.html")