from django.shortcuts import render

# Create your views here.
from security_tj.settings import CONTACT_TEL


def index(request):

    ret = {
        'tel': CONTACT_TEL,
        'title': 'title'
    }
    return render(request, 'index.html', ret)