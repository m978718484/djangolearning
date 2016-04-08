# Create your views here.
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime
from models import Book
from threading import Timer
import time



def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_time_upgrade(request):
    now = datetime.datetime.now()
    t = Template('<html><body>It is now {{ current_time }}.</body></html>')
    c = Context({'current_time':now})
    html = t.render(c)
    return HttpResponse(html)

def current_time_from_template(request):
    current_time = datetime.datetime.now()
    return render_to_response('current_time.html',{'current_time':current_time,'base':'base.html'})

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:12]
    return render_to_response('latest_books.html', {'book_list': book_list})
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hours_offset':offset,'next_time':dt})

def hello(request):
    return HttpResponse(request.get_host())

def current_url_view_good(request):
    return HttpResponse("Welcome to the page at %s" % request.path)

def meta_test(request):
    values = request.META.items()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))

def mate_template(request):
    values = request.META.items()
    return render_to_response('mytemplate.html',{'values':values})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title_icontains=q)
        return render_to_response('search_results.html', {'books': books,'query':q})
    else:
       return HttpResponse('error')
