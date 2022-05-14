from urllib import request
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def home(request):
     form = StudentRegistration()
     stud = User.objects.all()
     return render(request,'student/home.html',{'form':form,'stu':stud})

def login (request):
 return render(request,'student/login.html')