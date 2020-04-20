from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
# from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Partner
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# from .forms import LoginForm
from .forms import StoreForm


# Create your views here.
def index(request):
    ctx = {}
    if request.method == "GET":
        store_form = StoreForm()
        ctx.update({"form" : store_form})
    elif request.method == "POST":
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            store = store_form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect("/partner/")
        else:
            ctx.update({"form" : store_form})
    return render(request, "index.html", ctx)
#배민
# def login(request):
#     ctx = {}
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         loginID = request.POST.get("loginID")
#         loginPW = request.POST.get("loginPW")
#         user = authenticate(loginID=loginID, loginPW=loginPW)
#         if user is not None:
#             auth_login(request, user)
#             return redirect("/partner/")
#         else:
#             ctx.update({"error" : "사용자가 없습니다."})
#     return render(request, "login.html", ctx)

# def login(request): # 회원가입 누르면 다음 창 넘어가게 성공
#     ctx = {}
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             auth_login(request, user)
#             next_value = request.GET.get("next")
#             if next_value:
#                 return redirect(next_value)
#             else:
#                 return redirect("/partner/")
#         else:
#             ctx.update({"error" : "사용자가 없습니다."})
#     return render(request, "login.html", ctx)


# def sign_term00(request): # 정보 제공 동의 창
#     ctx = {}
#     return render(request, "sign_term00.html", ctx)



#회원가입 누르면 나오게하는 것 이름 학번 패스워드 올리기 =성공 .
# def signup(request):
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
         # try:
#         username = request.POST.get("username")
#         code = request.POST.get("code")
#         password = request.POST.get("password")
#         new_user = User.objects.create_user(username, code, password,)
        # except ValueError as e:
        #      pass
#     ctx = {}
#     return render(request, "signup.html", ctx)

# def get_object(self, id):
#     try:
#         return Partner.objects.get(pk=id)
#     except Partner.DoesNotExist:
#         return False


#성공
# def home(request):
#     user_id = request.session.get('user')
#     if user_id:
#         partner = Partner.objects.get(pk=user_id)
#         return HttpResponse(partner.loginID)
#     return HttpResponse('HOME!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/partner/')

# 성공
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        loginID = request.POST.get('loginID', None)
        loginPW = request.POST.get('loginPW', None)

        res_data = {}
        if not (loginID and loginPW):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            partner = Partner.objects.all()
            partner = Partner.objects.get(loginID=loginID)
            if check_password(loginPW, partner.loginPW):
                request.session['user'] = partner.id
                return redirect('/')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
        return render(request, 'login.html', res_data)

#성공
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        loginID = request.POST.get('loginID', None)
        loginPW = request.POST.get('loginPW', None)
        usernumber = request.POST.get('usernumber', None)
        usernumber2 = request.POST.get('usernumber2', None)
        re_password = request.POST.get('re-password', None)

        res_date = {}

        if not (username and loginID and loginPW):
            res_date['error'] = '모든 값을 입력해야합니다.'
        elif loginPW != re_password:
            res_date['error'] = '비밀번호가 다릅니다.'
        else:
            partner = Partner(
                loginID=loginID,
                username=username,
                usernumber=usernumber,
                usernumber2=usernumber2,
                loginPW=make_password(loginPW),
            )

            partner.save()
        return render(request, 'signup.html', res_date)


def login_agreed(request):
    return render(request, "login_agreed.html")

def sign_finish(request):
        return render(request, "sign_finish.html")

def edit_info(request):
    ctx = {}
    if request.method == "GET":
        store_form = StoreForm(instance=request.user.store)
        ctx.update({"form" : store_form})
    elif request.method == "POST":
        store_form = StoreForm(request.POST,instance=request.user.store)
        if store_form.is_valid():
            store = store_form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect("/partner/")
        else:
            ctx.update({"form" : store_form})
    return render(request, "edit_info.html", ctx)

def menu(request):
    ctx = {}
    # if request.user.is_anonymous or request.user.store is not None:
    #     return redirect("/partner/")
    # menu_list = Menu.objects.filter(store = request.user.store)
    # ctx.update({"menu_list": menu_list})

    return render(request, "menu_list.html", ctx)

def menu_add(request):
    ctx = {}
    return render(request, "menu_add.html", ctx)

# 회원가입 창 나와야함
#     elif request.method == "POST":
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username=request.POST["username"],password=request.POST["password1"]
#                 )
#             auth.login(request,user)
#             return redirect('home')
#     #     return render(request, "signup.html")
#     if request.method == "POST":
#         loginID = request.POST.get("loginID")
#         loginPW = request.POST.get("loginPW")
#         user = User.objects.create_user(loginID, loginPW)
#     ctx = {}
#     return render(request, "signup.html", ctx)
