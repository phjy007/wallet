from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response

# Create your views here.
def show_index(request):
	return render_to_response("html/index.html")

@login_required
def show_homepage(request, username):
	return render_to_response("html/homepage.html")

def show_someone_piggybank(request):
	return render_to_response("html/someone_piggybank.html")

@login_required
def show_new_article(request, username):
    return render_to_response("html/new_article.html")

@login_required
def show_view_article(request, username):
    return render_to_response("html/view_article.html")




def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print 'username=' + username
    print 'password=' + password
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/homepage/" + username + "/")
    else:
        return HttpResponseRedirect("/index/")


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")