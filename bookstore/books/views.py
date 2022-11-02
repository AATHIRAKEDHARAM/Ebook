from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,"books/master.html")

def booklist(request):
    return render(request,"books/user_books.html")

def home(request):
    return render(request,'books/user_home.html')

def profile(request):
    return render(request,'books/user_profile.html')

def login(request):
    return render(request,'books/cust_login.html')    

def custreg(request):
    return render(request,'books/cust_reg.html')      