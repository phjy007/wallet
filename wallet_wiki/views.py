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
    if username != request.user.username:
        return HttpResponseRedirect("/index/")
    return render_to_response("html/homepage.html", locals())


@login_required
def write_new_article(request, username):
    if username != request.user.username:
        return HttpResponseRedirect("/index/")
    return render_to_response("html/new_article.html", locals())


@login_required
def show_my_article(request, username, article_id):
    pass


@login_required
def show_my_collection(request, username, collection_id):
    pass


@login_required
def my_message(request):
    pass


@login_required
def visit_someone_piggybank(request, whose_home):
    username = request.user.username
    return render_to_response("html/someone_piggybank.html", locals())


@login_required
def view_article(request, author, article_id):
    username = request.user.username
    return render_to_response("html/view_article.html", locals())


@login_required
def view_collection(request, author, collection_id):
    username = request.user.username
    return render_to_response("html/view_article.html", locals())




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