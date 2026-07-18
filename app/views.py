from django.shortcuts import render
from celery_project.celery import debug_task

# Create your views here.
def index(request):
    debug_task.delay()
    return render(request,"index.html")
