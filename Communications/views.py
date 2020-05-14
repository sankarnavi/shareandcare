from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import(authenticate, get_user_model, login, logout)
from Communications.models import Contact
from product.models import Products
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# creating a string

# creating an instance of
# GeeksModel

# Create your views here.


@login_required
def Contactdetails(request, id):
    y = Products.objects.get(id=id)
    user = User.objects.get(username=y.Editor1.user)
    user_email = user.email
    res = Contact(Requester=request.user, JobtaskID=y,
                  Approver=user_email,)
    res.save()
    return redirect('/Products')


@login_required
def Accept(request, id):
    x = Contact.objects.get(id=id)
    x.status = "1"
    x.save()
    return redirect('/myprofile')


@login_required
def Reject(request, id):
    x = Contact.objects.get(id=id)
    x.status = "0"
    x.save()
    return redirect('/myprofile')


@login_required
def Delete(request, id):
    x = Products.objects.get(id=id)
    x.delete()
    return redirect('/myprofile')
