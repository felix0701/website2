from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, HttpResponse
import pyrebase
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
import requests
from social_django.models import UserSocialAuth
from django.contrib import messages
from django.conf import settings
from uk.recaptcha import validate_recaptcha
from django.urls import reverse
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import credentials, initialize_app
from django.contrib.auth.models import User
from uuid import uuid4



# Your Firebase configuration
config = {
    'apiKey': "AIzaSyACZuIa380Kr5EoSrxETB5aKrHizgq6OrY",
    'authDomain': "connectai-b2b54.firebaseapp.com",
    'databaseURL': "https://connectai-b2b54-default-rtdb.firebaseio.com",
    'projectId': "connectai-b2b54",
    'storageBucket': "connectai-b2b54.appspot.com",
    'messagingSenderId': "57138495378",
    'appId': "1:57138495378:web:3ccda313880744da824b4b",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()


def home(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        g_recaptcha_response = request.POST.get('g-recaptcha-response')

        try:
            # Validate reCAPTCHA
            recaptcha_is_valid = validate_recaptcha(g_recaptcha_response)

            if not recaptcha_is_valid:
                messages.error(request, "reCAPTCHA validation failed. Please try again.")
                return redirect('login')

            # Logout user to prevent automatic login
            logout(request)

            # Check if user exists in Firebase
            try:
                user = auth.sign_in_with_email_and_password(email, password)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 400:  # User does not exist
                    messages.error(request, "User does not exist. Please sign up.")
                    return redirect('signup')
                else:
                    raise  # Re-raise the exception if it's not a user not found error

            # Successful login, redirect to 'feed'
            print("Authentication successful. Redirecting to feed...")
            return redirect('feed')

        except Exception as e:
            print("Authentication error:", e)
            messages.error(request, "Login failed. Please check your credentials.")
            return redirect('login')  # Redirect back to login

    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        # Extract form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        g_recaptcha_response = request.POST.get('g-recaptcha-response')

        try:
            # Validate reCAPTCHA
            recaptcha_is_valid = validate_recaptcha(g_recaptcha_response)

            if not recaptcha_is_valid:
                messages.error(request, "reCAPTCHA validation failed. Please try again.")
                return redirect('signup')

            if password != confirm_password:
                messages.error(request, "Passwords do not match. Please try again.")
                return redirect('signup')

            # Check if the email is already registered
            if User.objects.filter(email=email).exists() or UserSocialAuth.objects.filter(provider='google-oauth2', uid=email).exists():
                messages.error(request, "This email is already registered.")
                return redirect('signup')

            # Create user with Firebase
            user = auth.create_user_with_email_and_password(email, password)

            # Redirect to fill_details.html after successful signup
            return redirect('fill_details')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('signup')

    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('home')
def feed(request):
        return render(request, "feed.html")
def choose_options(request):
    return render(request, "choose_options.html")
def message(request):
    return render(request, "message.html")
def mainpage(request):
    return render(request, "mainpage.html",)

# Import the necessary modules
# ...

# Your existing imports...
# Your existing imports...

# Firebase Admin SDK initialization


def fill_details(request):
    if request.method == 'POST':
        # Extract form data
        full_name = request.POST.get('fullName')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        domain_area = request.POST.get('domainArea')
        skills = request.POST.get('skills')
        
        # Get uploaded files
        photo = request.FILES['photo']
        resume = request.FILES['resume']

        try:
            # Check if the user signed up with Google
            if request.user.is_authenticated and UserSocialAuth.objects.filter(user=request.user).exists():
                # If user signed up with Google, use a UUID for profile identification
                user_identifier = str(uuid4())
            else:
                # Otherwise, use the user's email
                user_identifier = request.user.email.replace('.', ',') if request.user.is_authenticated else None
            
            if not user_identifier:
                messages.error(request, "User not authenticated properly.")
                return redirect('home')

            # Upload files to Firebase Storage
            photo_url = storage.child("photos").child(user_identifier).put(photo)
            resume_url = storage.child("resumes").child(user_identifier).put(resume)

            # Get download URLs for the uploaded files
            photo_download_url = storage.child("photos").child(user_identifier).get_url(None)
            resume_download_url = storage.child("resumes").child(user_identifier).get_url(None)

            # Store data in Firebase Realtime Database
            user_data = {
                'full_name': full_name,
                'dob': dob,
                'address': address,
                'profession': profession,
                'domain_area': domain_area,
                'skills': skills,
                'photo_url': photo_download_url,
                'resume_url': resume_download_url
            }
            # Save data under the user's identifier in the Firebase database
            database.child('profiles').child(user_identifier).set(user_data)

            messages.success(request, "Profile created successfully!")
            return redirect('feed')  # Redirect to home or any other appropriate page
        except Exception as e:
            messages.error(request, str(e))
            return redirect('fill_details')  # Redirect back to fill_details page in case of error

    return render(request, 'fill_details.html')
