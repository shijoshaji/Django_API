from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    template = 'base.html'
    return render(request,template)


def about(request):
    return HttpResponse('Will add details about this app')
    

