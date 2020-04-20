from django.shortcuts import render

# Create your views here.

def main(req):
    return render(req, 'jhjapp/main.html', {})

def privacy(req):
    return render(req, 'jhjapp/privacy.html', {})

def service(req):
    return render(req, 'jhjapp/service.html', {})
