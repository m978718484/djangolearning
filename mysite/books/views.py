# Create your views here.

from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book

def search_form(request):
    return render_to_response('search_form1.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		return render_to_response('search_results.html',{'books':books,'query':q})
	else:
		return HttpResponse('Please submit a search term.')



def test(request):
	return HttpResponse('asdfasdfasdfasdfasdfasdfasdf')
	