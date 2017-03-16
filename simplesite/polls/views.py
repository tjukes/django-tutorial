from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in latest_question_list)
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "Results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question %s." % question_id)
