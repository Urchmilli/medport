from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AdmissionForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'patient/index.html')

def about(request):
    return render(request, 'patient/about.html')

def services(request):
    return render(request, 'patient/services.html')

def contact(request):
    return render(request, 'patient/contact.html')

def blog(request):
    return render(request, 'patient/blog.html')

def forgot_password(request):
    return render(request, 'patient/forgot_password.html')

def appointment_submitted(request):
    return render(request, 'patient/appointment_submitted.html')

# def signupSuccessful(request):
#     return render(request, 'patient/signup_successful.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['userID']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists! Please try some other username.')
            return render(request, 'patient/signup.html')
        
        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered')
            return render(request, 'patient/signup.html')
        
        if pass1 != pass2:
            messages.error(request, "Password did'nt match")
            return render(request, 'patient/signup.html')
            
        if not username.isalnum:
            messages.error(request, 'Username must be alpha numeric')
            return render(request, 'patient/signup.html')   
            
        myuser = User.objects.create_user(username = username, email=email, password = pass1, first_name=fname, last_name=lname )
        
        myuser.save()
        
        # messages.success(request, "your account has been successfully created.")
        return render(request, 'patient/signup_successful.html')
    
    return render(request, 'patient/signup.html')
    

    
def signin(request):
    if request.method =="POST":
        username = request.POST['userID']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None: 
            fname = user.first_name
            login(request, user)
            return render(request, "patient/dashboard.html", {'fname':  fname})    
        else:
            messages.error(request, "Bad cridentials")    
            return render(request, "patient/signin.html")

    return render(request, "patient/signin.html")


def dashboard(request):
    if request.method  == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        residential_address = request.POST['residential_address']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        date_admitted = request.POST['date_admitted']
        ward = request.POST['ward']
        phone_number = request.POST['phone_number']
        patient_id = request.POST['patient_id']
        symptoms = request.POST['symptoms']
        
        new_admission = AdmissionForm(first_name=first_name, last_name=last_name, residential_address=residential_address,
                                      date_of_birth=date_of_birth, gender=gender, date_admitted=date_admitted, ward=ward, 
                                      phone_number=phone_number, patient_id=patient_id, symptoms=symptoms)
        new_admission.save()
        # messages.success(request, "A doctor will attend to you shortly.")
        return redirect('appointment_submitted')
    
        
    return render(request, 'patient/dashboard.html') 

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('index')
 

        
        
        
        
    
