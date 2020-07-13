from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'home.html', {'name': 'Bhavesh'})
	
def add(request):
	first = request.GET["txtFirst"]
	return render(request, 'result.html', {'first': first})