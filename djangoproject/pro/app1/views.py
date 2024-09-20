from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,'Username already exist please try some other username')


        if User.objects.filter(email=email):
            messages.error(request,'Email already registered!')


        if len(username)>10:
            messages.error(request,'Username must be under 10 characters')

        if pass1 != pass2:
            messages.error(request, 'password didnt match!')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-numeric!')


        myuser=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pass1)

        myuser.save()
        messages.success(request,"Your account has been successfully created.")

        return redirect('/login/')
    return render(request,'register.html')


def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        print(username,pass1)

        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            print('hii')
            login(request, user)
            return redirect('/')

        else:
            messages.error(request,'Bad Credentials!')
            # return redirect('/')

    return render(request,'login.html')


def product(request):
    if request.method == 'POST':
        productname=request.POST['productname']
        image=request.FILES['image']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        price=request.POST['price']
        my_field=request.POST['my_field']
        description=request.POST['description']
        p=Product.objects.create(productname=productname,image=image,image1=image1,image2=image2,price=price,my_field=my_field,description=description)
        return redirect('/views/')
    return render(request,'product.html')

# def product1(request):
#     pr=Product.objects.all()
#     return render(request, 'product1.html', {'pr': pr})

def productdelete(request,id):
    pr=Product.objects.get(id=id)
    print(pr)
    pr.delete()
    return redirect('/views/')

def productupdate(request,id):
    pr=Product.objects.get(id=id)
    if request.method == 'POST':
        productname = request.POST['productname']
        image = request.FILES.get('image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        price = request.POST.get('price')
        print(price)
        my_field = request.POST['my_field']
        description = request.POST['description']
        pr.productname=productname
        pr.price=price
        pr.my_field=my_field
        pr.description=description
        if image:
            pr.image=image
            pr.image1=image1
            pr.image2=image2
        pr.save()
        return redirect('/views/')
    return render(request,'productupdate.html',{'pr':pr})

def views(request):
    pr=Product.objects.all()
    return render(request, 'views.html', {'pr': pr})

@login_required(login_url='/login/')  #add product to login
def product(request):
    return render(request,'product.html')

def productviews(request,id):
    pr=Product.objects.all()
    return render(request,'productviews.html',{'pr':pr})
@login_required(login_url='/login/')
def addtocart(request,pid):
    user=request.user.id
    p=Product.objects.get(id=pid)
    print(p.id)
    if Cart.objects.filter(users=user,product=p):
        c=Cart.objects.get(users=user,product=p)
        c.quantity+=1
        c.save()
        return HttpResponse('product added in cart')

    else:
        cart=Cart.objects.create(product_id=p.id,users_id=user,total=p.price)
        return HttpResponse('product added in cart')

    return render(request,'cart.html')


@login_required(login_url='/login/')
def cart(request):
    user = request.user.id
    c=Cart.objects.filter(users=user)
    return render(request,'cart.html',{'c':c})

def logout_view(request):
    logout(request)
    return redirect('/')