from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home_wilogin.html')
    else:
        return redirect('/login')

def add(request):
    if request.user.is_authenticated:
        if(request.method=="POST"):
            itype = request.POST['itype']
            vtype = request.POST['vtype']
            manufacturer = request.POST['manufacturer']
            quantity = request.POST['quantity']
            price = request.POST['price']
            item = Item(i_type=itype, v_type=vtype, manufacturer=manufacturer, quantity=quantity, price=price)
            item.save()
            return redirect('/add')
        else:
            return render(request, 'add.html')
    else:
        return redirect('/login')

def view_login(request):
    if(request.method=="POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def signup(request):
    if(request.method=='POST'):
        username = request.POST['username']
        cnf_pwd = request.POST['cnf_password']
        pwd = request.POST['password']
        if(pwd==cnf_pwd):
            # form.save()
            # form.save()
            user = User(username=username, password=pwd)
            user.set_password(pwd)
            user.save()
            print(username)
            return redirect('/login')
        else:
            msg = "The password doesn't match"
            # form = signupForm()
            return render(request, 'signup.html', {'msg':msg})
    else:
        # form = signupForm()
        msg = ""
        return render(request, 'signup.html', {'msg':msg})
    
def do_logout(request):
    logout(request)
    return redirect('/login')

def list(request):
    if request.user.is_authenticated:
        items = Item.objects.all()
        return render(request, 'list.html', {'items':items})
    
def delete(request, id):
    item = Item.objects.filter(id=id)
    item.delete()

    return redirect('/view_delete')

def view_delete(request):
    items = Item.objects.all()
    return render(request, 'delete.html', {'items':items})

def edit(request, id):
    if(request.method=="POST"):
        item = Item.objects.get(id=id)
        item.i_type = request.POST.get('itype')
        item.v_type = request.POST.get('vtype')
        item.manufacturer = request.POST.get('manufacturer')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/list')
    else:
        items = Item.objects.filter(id=id)
        return render(request, 'edit.html', {'items':items})
    
def sale(request):
    if(request.method=="POST"):
        itype = request.POST['itype']
        quantity = int(request.POST['quantity'])
        item = Item.objects.filter(i_type=itype)[0]
        items = Item.objects.all()
        if(quantity<=int(item.quantity)):
            item.quantity = item.quantity - quantity
            item.save()
            cost = quantity*item.price
            sale = Sale(i_type = item.i_type, manufacturer = item.manufacturer, v_type = item.v_type, quantity = quantity, cost=cost)
            sale.save()
            return redirect('sale')
        else:
            msg = "Insufficient inventory!"
            return render(request, 'sale.html', {'msg':msg, 'items':items})
    else:
        items = Item.objects.all()
        return render(request, 'sale.html', {'items':items})
    
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales':sales})

def reorder(request):
    items = Item.objects.all()
    insufficients = []
    for item in items:
        if(item.quantity<10):
            insufficients.append(item)

    return render(request, 'reorder.html', {'insufficients':insufficients})