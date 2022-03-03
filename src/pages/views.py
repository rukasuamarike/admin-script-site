from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Script
from .forms import ScriptForm, RawScriptForm
import logging
logger = logging.getLogger(__name__)
logging.config.dictConfig({
        'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
    })

def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main/')
    else:
        form = UserCreationForm()
    return render(request, 'newuser.html', {'form': form})

def shell_send(request):
    form = RawScriptForm()
    if request.method == "POST":
        form = RawScriptForm(request.POST)
        if form.is_valid():
            Script.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "shellsend.html", context)

def home_view(request):
    form = RawScriptForm()
    if request.method == "POST":
        form = RawScriptForm(request.POST)
        if form.is_valid():
            Script.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request,"home.html",context)
        # HttpResponse("<h1>Home</h1>")

def hello_world(request,*args, **kwargs):

    return render(request,"hello.html",{})

@login_required


def panel(request,*args, **kwargs):
    k = User.is_staff
    logger.error(k)
    users = User.objects.all()
    context = {
            'userlist': users,
        }
    return render(request,"panel.html",context)

@login_required
@permission_required('User.is_staff')
def log(request):

    context = {

    }
    return render(request,'logs.html',context)
@login_required
def accountinfo(request):
    context = {
        'user':request.user
    }

    return render(request, 'accountinfo.html', context)