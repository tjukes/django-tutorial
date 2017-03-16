from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the polls index.")

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)
