
from django.http import HttpResponse

from django.shortcuts import render, HttpResponseRedirect

from django.shortcuts import render_to_response

from datetime import datetime

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
#    return HttpResponse("Hello worls ! ")
    return render(request, 'hello.html', context)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')


def search2(request):
    if 'q2' in request.GET:
        message = 'You searched for : %r' % request.GET['q2']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def test_formView(request):
    now = datetime.now()
    if request.method == "POST":
        Time1 = request.POST['Time1']
        Time2 = request.POST['Time2']
        if Time1 < now < Time2:
            now1 = datetime.now()
            return render_to_response("test_form.html", {"time": "now1"})
    return HttpResponseRedirect("test_form.html")
