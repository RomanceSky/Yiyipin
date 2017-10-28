from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
#from .models import Book

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def contact(request):

    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', '1212@exapmle.com'),
                ['siteowner@example.com'],        
            )
            return HttpResponseRedirect('/')
    return render_to_response('errors_form.html', {'errors': errors})
"""
def latest_books(request):
        book_list = Book.objects.order_by('-pub_date')[:10]
        return render_to_response('latest_books.html', {'book_list':book_list})
"""
def hours_ahead(request, offset):
        try:
                offset = int(offset)
        except ValueError:
                raise Http404()
        dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
        html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
        return HttpResponse(html)



