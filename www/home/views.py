from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
 
# Create your views here.
# def index(request):
#     return HttpResponse("Hello, World!")

# def error(request):
#     return HttpResponseNotFound('<h1>not found</h1>')
#     #raise Http404("Not Found")


def index(request):
    msg = 'My Message'
    return render(request, 'home/index.html', {'message': msg})