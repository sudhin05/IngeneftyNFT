from django.shortcuts import render, HttpResponse

def index(request):
    dic = {
        'variable1':'1',
        'variable2':'2',
        'variable3':'3'
    }
    return render(request, 'index.html',dic)


def about(request):
    return HttpResponse('hello')
    