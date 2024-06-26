from django.shortcuts import render,redirect
from Backend.models import productdb,bigdb
from Webapp.models import conytactdb,registerdb,cartdb,paymentdb
from django.contrib import messages
import razorpay

# Create your views here.
def home_page(x):
    cat=bigdb.objects.all()
    return render(x,"home.html",{'cat':cat})
def about_page(x):
    cat = bigdb.objects.all()
    return render(x,"about.html",{'cat':cat})

def contact_page(x):
    cat = bigdb.objects.all()
    messages.success(x, "We Will Contact You Soon")
    return render(x,"contact.html",{'cat':cat})

def our_product(x):
    cat = bigdb.objects.all()
    data=productdb.objects.all()
    return render(x,"ourproduct.html",{'data':data,'cat':cat})

def save_contact(x):
        if x.method == "POST":
            na = x.POST.get('name')
            em = x.POST.get('email')
            ph = x.POST.get('phone')
            su = x.POST.get('subject')
            me = x.POST.get('message')
            obj = conytactdb(Name=na, Email=em, Phone=ph, Subject=su,Messege=me)
            obj.save()
            return redirect(contact_page)

def filter_page(x,cat_name):
    cat=bigdb.objects.all()

    data=productdb.objects.filter(Category=cat_name)
    return render(x,"product_filter.html",{'data':data,'cat':cat})

def single_page(x,proid):
    cat=bigdb.objects.all()
    data=productdb.objects.get(id=proid)
    return render(x,"single_product.html",{'data':data,'cat':cat})

def register_page(x):
    return render(x,"Register.html")

def register_save(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        em=request.POST.get('Email')
        pas=request.POST.get('Pas1')
        obj=registerdb(Username=na,Email=em,Password=pas)
        if registerdb.objects.filter(Username=na).exists():
            messages.warning(request,"Username already exists")
        elif registerdb.objects.filter(Email=em).exists():
            messages.warning(request,"Email already exists")
        else:
            obj.save()
            messages.success(request,"Signup Successfully")
        return redirect(register_page)

def user_login(request):
    if request.method=="POST":
        un=request.POST.get('Name')
        pas=request.POST.get('Password')
        if registerdb.objects.filter(Username=un,Password=pas).exists():
            request.session['Username']=un
            request.session['Password']=pas
            messages.success(request, "login  successfully")
            return redirect(home_page)
        else:
            return redirect(register_page)

    else:
        return redirect(register_page)

def user_logout(request):
    del request.session['Username']
    del  request.session['Password']
    messages.success(request, "logout  successfully")
    return redirect(home_page)

def save_cart(x):
    if x.method == "POST":
        us = x.POST.get('Username')
        pr = x.POST.get('Product_Name')
        qn = x.POST.get('Quantity')
        tot = x.POST.get('Total')
        obj = cartdb(Username=us,Product_Name=pr,Quantity=qn,Total_price=tot)
        obj.save()
        messages.success(x,"Add Successfully")
        return redirect(home_page)

def cart_page(request):
    cat = bigdb.objects.all()
    data=cartdb.objects.filter(Username=request.session['Username'])
    subtotal=0
    shipping_charge=0
    total=0
    for i in data:
        subtotal+=i.Total_price
    if subtotal>=500:
        shipping_charge=50
    else:
        shipping_charge=100
    total=subtotal+shipping_charge
    return render(request,"Cart.html",{'data':data,'subtotal':subtotal,'cat':cat,'total':total,'shipping_charge':shipping_charge})

def delet_cart(x,pid):
    y=cartdb.objects.filter(id=pid)
    y.delete()
    messages.error(x,"Item Removed")
    return redirect(cart_page)

def user_page(x):
    return render(x,"Userlogin.html")

def checkout_page(request):
    cat = bigdb.objects.all()
    products=cartdb.objects.filter(Username=request.session['Username'])
    subtotal=0
    total=0
    shipping_charge=0
    for i in products:
        subtotal=subtotal+i.Total_price
    if subtotal>500:
        shipping_charge=50
    else:
        shipping_charge=100
    total=shipping_charge+subtotal
    return render(request,"checkout.html",{'products':products,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge,'cat':cat})

def payment_page(request):
    #retrieve the orderdb objects with the specified id
    customer=paymentdb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    pay=customer.Total_price
    amount=int(pay*100)

    #convert amount to string for pring
    pay_str=str(amount) #accusing payment amount in rupees

    #printing each charactor of the payment amount
    for i in pay_str:
        print(i)
    if request.method == "POST":
        order_currency = 'INR'
        client=razorpay.Client(auth=('rzp_test_Vhx69IuMfkbIPZ','iLNdHlWTEpE23GBiKvIBfeIJ'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})

def save_payment(x):
    if x.method=="POST":
        na=x.POST.get('Name')
        em=x.POST.get('Email')
        ad=x.POST.get('Address')
        ph=x.POST.get('Phone')
        sa=x.POST.get('bill')
        tot=x.POST.get('Total')
        obj=paymentdb(Name=na,Email=em,Address=ad,Phone=ph,Say=sa,Total_price=tot)
        obj.save()
        return redirect(payment_page)









