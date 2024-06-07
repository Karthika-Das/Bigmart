from django.shortcuts import render,redirect
from Backend.models import bigdb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Webapp.models import conytactdb
from django.contrib import messages

# Create your views here.
def index_page(x):
    return render(x,"index.html")
def category_page(x):
    return render(x,"category.html")

def save_page(x):
    if x.method=="POST":
        cna=x.POST.get('Name')
        des=x.POST.get('Description')
        im=x.FILES['Image']
        obj=bigdb(Cname=cna,Description=des,Image=im)
        obj.save()
        messages.success(x,"category saved successfully")
        return redirect(category_page)

def display_page(x):
    data=bigdb.objects.all()
    return render(x,"display.html",{'data':data})

def edit_page(x,bigid):
    data=bigdb.objects.get(id=bigid)
    return render(x,"edit.html",{'data':data})

def update_page(x,bigid):
    if x.method=="POST":
        cna=x.POST.get('Name')
        des=x.POST.get('Description')
        try:
            im=x.FILES['Image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=bigdb.objects.get(id=bigid).Image
        bigdb.objects.filter(id=bigid).update(Cname=cna,Description=des,Image=file)
        return redirect(display_page)

def delete_page(x,bigid):
    y=bigdb.objects.filter(id=bigid)
    y.delete()
    messages.error(x,'deleted')
    return redirect(display_page)

def login_page(request):
    return render(request,"admin_login.html")

def admin_page(request):
    if request.method=="POST":
        un=request.POST.get('Username')
        pas=request.POST.get('Password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pas)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pas
                messages.success(request,"welcome")
                return redirect(index_page)
            else:
                messages.error(request,"invalid password")
                return redirect(login_page)
        else:
            messages.warning(request,"user not found")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logout successfully")
    return redirect(login_page)

def product_page(x):
    cat=bigdb.objects.all()
    return render(x,"product.html",{'cat':cat})
def save_product(x):
    if x.method=="POST":
        ca=x.POST.get('Category')
        pro=x.POST.get('Product')
        de=x.POST.get('Description')
        pr=x.POST.get('Price')
        im=x.FILES['Image']
        obj=productdb(Category=ca,Product=pro,Description=de,Price=pr,Image=im)
        obj.save()
        messages.success(x,"saved successfully")
        return redirect(product_page)

def product_display(x):
    data=productdb.objects.all()
    return render(x,"productdisplay.html",{'data':data})

def product_edit(x,proid):
    pro=productdb.objects.get(id=proid)
    cat = bigdb.objects.all()
    return render(x,"productedit.html",{'pro':pro,'cat':cat})

def update_product(x,proid):
    if x.method=="POST":
        ca=x.POST.get('Category')
        pro=x.POST.get('Product')
        de=x.POST.get('Description')
        pr=x.POST.get('Price')
        try:
            im=x.FILES['Image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=proid).Image
        productdb.objects.filter(id=proid).update(Category=ca,Product=pro,Description=de,Price=pr,Image=file)
        messages.success(x,"successfully updated")
        return redirect(product_display)


def delete_product(x,proid):
    y=productdb.objects.filter(id=proid)
    y.delete()
    messages.error(x,"deleted")
    return redirect(product_display)

def data_details(x):
    data=conytactdb.objects.all()
    return render(x,"contactdata.html",{'data':data})

def delete_contact(x,delid):
    y=conytactdb.objects.filter(id=delid)
    y.delete()
    return redirect(data_details)




