from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from forms import ContactForm


def contact_form(request):
    errors = []
    if request.method=='POST':
        if not request.POST.get('subject',''):
            errors.append('enter a subject.')
        elif not request.POST.get('message',''):
            errors.append('enter a message.')
        elif not request.POST.get('email','') or '@' not in request.POST['email']:
            errors.append('enter a valid e-mail address.')
        if not errors:
            return HttpResponse('send mail done!')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('send mail done!')
    else:
        form = ContactForm()
    return render_to_response('contact_form1.html',{'form':form})