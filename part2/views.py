from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def _login(req):
    if req.method == 'POST':
        try: 
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(req, user)
                return render(req, 'part2/Home.html', {'username':username})
            return render(req, 'part2/Index.html', {'message': "Invalid Credentials"})
        except:
            return render(req, 'part2/Index.html', {'message': "Something went wrong"})
    return render(req, 'part2/index.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        confirmPassword = req.POST.get('confirmPassword')
        firstname = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        gender = req.POST.get('gender')
        if password == confirmPassword:
            try:
                user = User.objects.create_user(
                    username=username, 
                    password=password,
                    first_name=firstname,
                    last_name=lastName,
                    email=email)
                userprofile = UserProfile(user=user, gender=gender, phone=phone)
                userprofile.save()
                login(req, user)
                return render(req, "part2/Home.html", {'username': username})
            except:
                return render(req, 'part2/Signup.html', {'error':'Username already exists!'})
        return render(req, 'part2/Signup.html', {'error': 'Both passwords do not match.'})
    return render(req, 'part2/Signup.html')


def _logout(req):
    if req.method == 'POST':
        try:
            logout(req)
            return render(req, 'part2/Index.html', {'message':'Logged out successfully!'})
        except:
            return render(req, 'part2/Home.html', {'error':'Error while logging out!'})

