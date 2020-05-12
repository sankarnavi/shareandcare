from django.shortcuts import render, redirect
from django.http import request
from .models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm
from product.forms import ProductEntry
from django.contrib.auth.models import User
from product.models import Author
from django.contrib import messages
from django.http.response import HttpResponse
from Communications.models import Contact


@login_required
def Entry(request):
    if request.method == 'POST':
        form = ProductEntry(request.POST, request.FILES)

        if form.is_valid():
            sa = form.save(commit=False)
            sa.Editor1 = Author.objects.get(user=request.user)
            sa.save()
            return redirect('/')
    else:
        form = ProductEntry()
    return render(request, 'entry.html', {'form': form})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def home(request):
    x = Products.objects.all()
    return render(request, 'index.html', {"x": x})


@login_required
def Product(request):
    x = Products.objects.all()
    paginator = Paginator(x, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    context = {
        "x": paginator_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'products.html', context)


@login_required
def Productdetails(request, id):
    y = Products.objects.get(id=id)
    x = Products.objects.all
    z = Contact.objects.filter(Requester=request.user, JobtaskID=y)
    a = {
        'y': y,
        'x': x,
        'z': z
    }
    print(z)
    return render(request, 'prodetail.html', a)


@login_required
def myprofile(request):
    x = Products.objects.filter(Editor1=Author.objects.get(user=request.user))
    y = request.user
    z = Contact.objects.filter(Approver=request.user.email, status='69')
    a = {
        'y': y,
        'x': x,
        'z': z,
    }
    return render(request, 'profile.html', {"a": a})
