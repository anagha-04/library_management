from django.shortcuts import render,redirect

from django.views.generic import View

from user_app.models import User

from django.contrib.auth import authenticate,login,logout

# Create your views here.

class UserRegistrationView(View):

    def get(self,request):

        return render(request,"register.html")
    
    def post(self,request):

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        email = request.POST.get("email")

        password = request.POST.get("password")

        User.objects.create(first_name = first_name, last_name = last_name , email = email , password= password)

        return render(request,"register.html")
    
class LoginView(View):

    def get(self,request):

        return render(request,"login.html")
    
    def post(self,request):

        first_name = request.POST.get("first_name")

        password = request.POST.get("password")

        user = authenticate(first_name= first_name,password=password)

        if user:

            login(user)

            return redirect("register.html")
        
        return redirect("login.html")






