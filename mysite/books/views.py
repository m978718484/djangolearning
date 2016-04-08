# Create your views here.

from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book
from django.core.mail import send_mail
from mysite.contact.forms import ContactForm

#def search_form(request):
    #return render_to_response('search_form1.html')

# def search(request):
# 	if 'q' in request.GET and request.GET['q']:
# 		q = request.GET['q']
# 		books = Book.objects.filter(title__icontains=q)
# 		return render_to_response('search_results.html',{'books':books,'query':q})
# 	else:
# 		return HttpResponse('Please submit a search term.')

def search_form(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = 'Please submit a search term'
        elif len(q)>20:
            error = 'title length more than 20'
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books,'query':q})
    return render_to_response('search_form1.html',{'error':error})


def test(request):
    return HttpResponse('asdfasdfasdfasdfasdfasdfasdf')


	
def contact_form(request):
    errors = []
    if request.method=='POST':
        if not request.POST.get('subject',''):
            errors.append('enter a subject.')
        elif not request.POST.get('message',''):
            errors.append('enter a message.')
        elif not request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('enter a valid e-mail address.')
        if not errors:
            return HttpResponse('send mail done!')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })