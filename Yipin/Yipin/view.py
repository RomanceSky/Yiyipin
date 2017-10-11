
#from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
#    return HttpResponse("Hello worls ! ")
    return render(request, 'hello.html', context)
