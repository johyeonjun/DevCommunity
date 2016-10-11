# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.core.context_processors import csrf
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def login(request):

    return render(request, 'login.html')

def register(request):
    print 'hi'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print 'hello'
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    print "실패"
    return render_to_response('login.html', token)

def registration_complete(request):
    print "hi"
    return render_to_response('login.html')