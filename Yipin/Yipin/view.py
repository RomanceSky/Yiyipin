
from django.http import HttpResponse

from django.shortcuts import render

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
