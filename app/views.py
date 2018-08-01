from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
from app.models import User
from passlib.handlers.pbkdf2 import pbkdf2_sha256


@csrf_protect
def main(request):
    return render(request, '../static/index.html', {'photo': "mid"})




@csrf_exempt
def signup(request):
    if request.method == 'POST' or request.is_ajax():
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        hash_pass = pbkdf2_sha256.__hash__(password)

        User.objects.create(name=name, email=email, password=hash_pass)

        request.session['user'] = name
        print(request.session['user'])
        return render(request,"../static/index.html", {'username': request.session['user']})

def loggedin(request):

    print(request.session.get('user',None))
    if request.session.get('user',None) is not None:
        print('user is ',request.session['user'])
        return render(request,"../static/index.html", {'username': request.session['user']})
    else:
        return render(request,"../static/index.html")




@csrf_exempt
def checkForm(request):
    if request.method == 'POST' or request.is_ajax():
        response = ""
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(email=email):
            response += "این ایمیل قبلا ثبت شده است | "
        if password1 != password2:
            response += "رمز عبور با تایید آن برابر نیست"

        return HttpResponse(response)

