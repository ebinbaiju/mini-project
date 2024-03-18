from django.shortcuts import render,redirect,get_object_or_404
from .models import customer,staff,products
from .forms import AddForm,product_form
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def product(request):
    return render(request,"product.html")

def cart(request):
    return render(request,"cart.html")

def insert(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        customer(name=name,age=age,gender=gender,email=email,phonenumber=phonenumber,username=username,password=password,).save()
    return render(request,"customer.html") 


def view(request):
    er = customer.objects.all()
    return render(request,"view.html",{'er':er})


def detailedview(request,pk):
    er = customer.objects.get(id=pk)
    return render(request,"detailedview.html",{'er':er})


def delete(request,pk):
    er = customer.objects.get(id=pk)
    er.delete()
    return redirect("/")


def update(request,pk):
    er = customer.objects.get(id=pk)
    form = AddForm(instance = er)
    if request.method =="POST":
        form = AddForm(request.POST,instance = er)
        if form.is_valid:
            form.save()
            return redirect("/")
    return render(request,"update.html",{'form':form}) 

def customerlogin(request):
    return render(request,"customerlogin.html")


def userlog(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        er = customer.objects.filter(username=username,password=password)
        if er:

            user_details=customer.objects.get(username=username,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
            email = user_details.email


            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            request.session['email']=email

            send_mail(
                "login",
                "login successfully",
                "ebinhp88@gmail.com",
                [email],
                fail_silently=False,
            )

            return redirect('customerwelcome')
        else:
            return render(request,'customerlogin.html'),
    else:
        return render(request,'view.html')



def customerwelcome(request):
    id=request.session['id']
    name=request.session['name']
    age=request.session['age']
    return render(request,"customerwelcome.html",{'id':id,'name':name,'age':age})


def logoutuser(request):
    logout(request)
    return redirect('home')


def adminlogin(request):
    return render(request,"adminlogin.html")


def alog(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('adminlogin')
    else:
        return render(request,"adminlogin.html")
    

def input(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        approval = request.POST.get('approval')
        staff(name=name,age=age,gender=gender,email=email,phonenumber=phonenumber,username=username,password=password,approval=approval).save()
    return render(request,"staff.html") 

def view1(request):
    es = staff.objects.all()
    return render(request,"view1.html",{'es':es})


def detailedview1(request,pk):
    es = staff.objects.get(id=pk)
    return render(request,"detailedview1.html",{'es':es})


def delete1(request,pk):
    es = staff.objects.get(id=pk)
    es.delete()
    return redirect("staffwelcome")


def update1(request,pk):
    es = staff.objects.get(id=pk)
    form = AddForm(instance = es)
    if request.method =="POST":
        form = AddForm(request.POST,instance = es)
        if form.is_valid:
            form.save()
            return redirect("staffwelcome")
    return render(request,"update1.html",{'form':form}) 

def stafflogin(request):
    return render(request,"stafflogin.html")

def stafflog(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        es = staff.objects.filter(username=username,password=password,approval=True)
        if es:

            user_details=staff.objects.get(username=username,password=password)
            id=user_details.id
            name=user_details.name
            age=user_details.age
           


            request.session['id']=id
            request.session['name']=name
            request.session['age']=age
            

            
            return redirect('staffwelcome')
        else:
            error='invalid credentials or not approved by admin yet'
            return render(request,'stafflogin.html', {'error':error})
    else:
        return render(request,'view1.html')



def staffwelcome(request):
        id=request.session['id']
        name=request.session['name']
        age=request.session['age']
        form = product_form()
        if request.method =='POST':
            form = product_form(request.POST,request.FILES)
            if form.is_valid():
                form.save()
        es =  products.objects.all()       
        return render(request,"staffwelcome.html",{'id':id,'name':name,'age':age,'form':form,'es':es})


def logoutuser1(request):
    logout(request)
    return redirect('stafflogin')


def add_product(request):
    if request.method == 'POST':
        form = product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staffwelcome')  # Redirect to a view displaying all products
    else:
        form = product_form()
    return render(request, 'staffproduct.html', {'form': form})


def staffproduct_update(request,pk):
    es = products.objects.get(id=pk)
    form =product_form(instance=es)
    if request.method =='POST':
        form=product_form(request.POST, instance=es)
        if form.is_valid():
            form.save()
            return redirect('staffwelcome')
    return render(request, 'staffproduct_update.html',{'form':form})


# def staffproduct_update(request, pk):
#     try:
#         es = products.objects.get(id=pk)
#         return render(request, 'staffproduct_update.html', {'es': es})
#     except products.DoesNotExist:
#         return render(request, 'staffwelcome.html')


# def product_update(request, product_id):
#     products = get_object_or_404(products, pk=product_id)
#     if request.method == 'POST':
#         form = product_form(request.POST, instance=products)
#         if form.is_valid():
#             form.save()
#             return redirect('staffproduct_update', product_id=products.id)
#     else:
#         form = product_form(instance=products)
#     return render(request, 'staffwelcome.html', {'form': form})