from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
	return render(request, 'index.html')


def current_time(request):
    return HttpResponse('<h1>{}</h1>'.format(datetime.now()))