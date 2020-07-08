from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Pandey'})

def login(request):
    uname = request.GET['username']
    pwd = request.GET['password']

    if(uname==pwd):
        return render(request,'index.html',{'message':'Your logged in successfully'})
    else:
        return render(request,'index.html',{'message':'Your log in failed'})    

   

