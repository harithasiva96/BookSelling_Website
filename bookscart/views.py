from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookscart.models import customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from bookscart.models import admin_addbooks
from bookscart.models import buynow
from bookscart.models import payment
# Create your views here.

def home(request):
    return render(request,template_name='subpage.html')

def user_home(request):
    return render(request,template_name='login_home.html')


def form(request):
    if request.method=="POST":
        a=request.POST["first_name"]
        b=request.POST["last_name"]
        c=request.POST["age"]
        d=request.POST["place"]
        e=request.POST["phone"]
        f=request.POST["email"]
        g=request.POST["username"]
        h=request.POST["password"]
        i=customer(first_name=a,last_name=b,age=c,place=d,phone=e,email=f,username=g,password=h)
        i.save()
        i1=User(username=g,first_name=a,last_name=b,email=f)
        i1.set_password(h)
        i1.save()
        return HttpResponse('<script>alert("Registered Successfully"),window.location="/login";</script>')
    return render(request,template_name='reg_form.html')

def admin_home(request):
    return render(request,template_name='admin_home.html')
def login(request):
    if request.method=="POST":
        x=request.POST['username']
        y=request.POST['password']
        au=authenticate(username=x,password=y)
        print(au)
        request.session['member_id']=x
        if au is not None and au.is_superuser==1:
            return redirect(admin_home)
        else:
            z=customer.objects.get(username=x)
            if z.password==y:
                if au is not None and au.is_superuser==0:
                    return render(request,template_name='login_home.html')
    return render(request,template_name='login.html')


def edit(request):
    user_id=request.session['member_id']
    o=customer.objects.get(username=user_id)
    o1=User.objects.get(username=user_id)
    if request.method=='POST':
        o.first_name=request.POST['first_name']
        o.last_name=request.POST['last_name']
        o.age=request.POST['age']
        o.place=request.POST['place']
        o.phone=request.POST['phone']
        o.email=request.POST['email']
        o.save()
        o1.first_name=request.POST['first_name']
        o1.last_name=request.POST['last_name']
        o1.email=request.POST['email']
        o1.save()
        return HttpResponse('<script>alert("Profile updated"),window.location="/userhome";</script>')
    return render(request,template_name='edit.html',context={'u':o})

def log_out(request):
    logout(request)
    return redirect(home)

def addbooks(request):
    if request.method=="POST":
        p=request.POST['book_name']
        q=request.FILES['photo']
        r=request.POST['price']
        s=request.POST['author']
        t=admin_addbooks(book_name=p,photo=q,price=r,author=s)
        t.save()
        return HttpResponse('<script>alert("Saved Successfully"),window.location="/books";</script>')
    return render(request,template_name='admin_addbooks.html')

def viewbooks(request):
    k=admin_addbooks.objects.all()
    return render(request,template_name='viewbooks.html',context={'k1':k})

def update_books(request,id):
    p_id=id
    q=admin_addbooks.objects.get(id=p_id)
    if request.method=="POST":
        q.book_name=request.POST['book_name']
        q.photo=request.FILES['photo']
        q.price=request.POST['price']
        q.author=request.POST['author']
        q.save()
        return HttpResponse('<script>alert("Updated Successfully"),window.location="/books";</script>')
    return render(request,template_name='viewbooks.html',context={'p':q})

def deletion(request,id1):
    pid=id1
    q=admin_addbooks.objects.get(id=pid)
    q.delete()
    return HttpResponse('<script>alert("Deleted Successfully"),window.location="/books";</script>')

def customer_viewbooks(request):
    k=admin_addbooks.objects.all()
    return render(request,template_name='customer_viewbooks.html',context={'k1':k})

def buy(request,id2):
    uid=request.session['member_id']
    b_id=id2
    print(b_id)
    q= admin_addbooks.objects.get(id=b_id)
    pr=q.price
    print(pr)
    b_name=q.book_name
    print(b_name)
    if request.method=="POST":
        qnt=request.POST['quantity']
        total=int(qnt)*int(pr)
        print(total)
        x=buynow(book_id=b_id,book_name=b_name,quantity=qnt,price=pr,user_id=uid,status="pending",amount=total)
        x.save()
        return HttpResponse('<script>alert("successfully ordered"),window.location="/userhome";</script>')
    return render(request,template_name='checkout.html')


def view_order1(request):
    f=buynow.objects.all()
    return render(request,template_name='admin_vieworder.html',context={'f1':f})

def order_approval(request,id3):
    rid=id3
    f=buynow.objects.get(id=rid)
    f.status="Approved"
    f.save()
    return HttpResponse('<script>alert("Approved Successfully"),window.location="/view1";</script>')

def order_rejection(request,id3):
    rid=id3
    f=buynow.objects.get(id=rid)
    f.status="Rejected"
    f.save()
    return HttpResponse('<script>alert("Rejected Successfully"),window.location="/view1";</script>')

def user_vieworder(request):
    sid=request.session['member_id']
    f=buynow.objects.filter(user_id=sid)
    return render(request,template_name='user_vieworder.html',context={'s1':f})

def paymentRegistration(request,id4,amount):
    uid=request.session['member_id']
    tid=id4
    amt=amount
    if request.method == "POST":

        q=payment(user_id=uid, book_id=tid, total=amt,  status="Paid")
        q.save()
        o=buynow.objects.get(id=tid,user_id=uid)
        o.status="Paid"
        o.save()
        return HttpResponse('<script>alert("Payment Successful"),window.location="/my_orders";</script>')
    return render(request,template_name='payment.html',context={'p':amt})
