from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def galery(request):
    return render(request, 'blog/galery.html', {})

def form(request):
    return render(request, 'blog/form.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})