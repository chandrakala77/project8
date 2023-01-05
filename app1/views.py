from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def htmlfile1(request):
    return HttpResponse('this is htmlfile1')
