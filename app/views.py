import datetime
import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
from app.models import User, Cloth, Photo


@csrf_protect
def main(request):
    return render(request, '../staticFolder/index.html',
                  {'username': request.session.get('user', None), 'list': "hello my freind"})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('uname', None)
        password = request.POST.get('psw', None)
        print("clear_pass:"+str(password))

        md = hashlib.md5()
        md.update(password.encode("utf-8"))
        # hash_pass = pbkdf2_sha256.__hash__(password)
        hash_pass = md.hexdigest()
        print("hashed_pass: " + str(hash_pass))

        if User.objects.filter(email=email).exists():
            error = "این ایمیل قبلا ثبت شده است !!"
            return render(request, "../staticFolder/register.html",
                          {'username': request.session.get('user', None), 'error': error})

        if name is not None and phone is not None and email is not None and password is not None:
            User.objects.create(name=name, email=email, password=hash_pass)
            request.session['user'] = name

            return render(request, "../staticFolder/index.html", {'username': request.session.get('user', None)})
    else:
        return render(request, "../staticFolder/register.html", {'username': request.session.get('user', None)})


@csrf_exempt
def login(request):
    if request.method == 'POST':

        email = request.POST.get('uname', None)
        password = request.POST.get('psw', None)

        if email is not None and password is not None:

            print(password)

            md = hashlib.md5()
            md.update(password.encode("utf-8"))
            # hash_pass = pbkdf2_sha256.__hash__(password)
            hash_pass = md.hexdigest()
            print(hash_pass)

            if User.objects.filter(email=email, password=hash_pass).exists():
                user = User.objects.get(email=email)
                request.session['user'] = user.name
                username = request.session['user']
                return render(request, '../staticFolder/index.html', {'username': username})
            else:
                error = "نام کاربری و یا کلمه ی عبور اشتباه است"
                return render(request, '../staticFolder/login.html',
                              {'error': error, 'usermane': request.session.get('user', None)})
        else:
            return HttpResponse("لطفاایمیل و رمزعبور خود را به درستی وارد کنید")

    else:

        return render(request, '../staticFolder/login.html', {'username': request.session.get('user', None)})


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


def showItems(request):
    sex = request.GET.get("sex", None)
    categ = request.GET.get("category", None)
    clothList = Cloth.objects.all()
    print("first" + str(clothList.values()))
    if categ is not None:
        clothList = clothList.filter(category=categ)

    if sex is not None:
        clothList = clothList.filter(sex=sex)
    print(clothList.values())
    return render(request, '../staticFolder/shop.html', {'list': clothList, 'username': request.session.get('user', None)})


def contact(request):
    return render(request, "../staticFolder/contact.html", {'username': request.session.get('user', None)})


def about(request):
    return render(request, "../staticFolder/about.html", {'username': request.session.get('user', None)})

@csrf_exempt
def notFount(request):
    return render(request, "../staticFolder/404.html", {'username': request.session.get('user', None)})

@csrf_exempt
def singleItem(request):
    item = request.GET.get("item", None)

    if item is not None:
        mainItem = Cloth.objects.get(name=item)
        print(mainItem)

        return render(request, "../staticFolder/single.html",
                      {"item": mainItem, 'username': request.session.get('user', None)})
    else:
        return render(request, "../staticFolder/404.html", {'username': request.session.get('user', None)})
@csrf_exempt
def checkout(request):
    i = datetime.datetime.today()
    end = i + datetime.timedelta(days=4)
    item = {'size': 20, 'returnDate': "16.  4.97", 'name': "لباس۱", 'rentPrice': "12000"}

    if request.method == "POST":
        pass
    return render(request, "../staticFolder/checkout.html", {'item':item})

def exit(request):

    del request.session['user']

    return redirect("/main")

@csrf_exempt
def payment(request):

    return render(request, '../staticFolder/payPage.html',{'username': request.session.get('user', None)})