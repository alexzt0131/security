from django.shortcuts import render

# Create your views here.

def index(request):

    ret = {
        'tel': '13888888888',
        'title': 'title'
    }
    return render(request, 'index.html', ret)