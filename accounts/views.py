from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .forms import CreateUserForm, CustomLoginForm
from django.core.mail import send_mail, BadHeaderError
from .models import Profile

# REST framework
from rest_framework import generics
from .serializers import ProfileSerializer


def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save() # user is saved in DB
            
            try:
                profile, created = Profile.objects.get_or_create(user=user) # user Profile created

                send_mail( # Sending message with the code
                    "Hi! It's Alikhan.",
                    f'Here is your code to continue registration: {profile.confirmation_code}',
                    'alserikbolov@mail.ru',
                    [user.email],
                    fail_silently=False,
                )

                return redirect('accounts:confirm_email')
            
            # Email error message
            except BadHeaderError:
                user.delete() # deleting user from DB if error appears
                error_message = "Email is not exist. Please check it again."
            except Exception as e:
                user.delete()
                error_message = f"This email is not exist. Please write another one."
                
            return render(request, 'registration/register.html', {'form':form, 'error': error_message})
            
    else:
        form = CreateUserForm()
        
    
    return render(request, 'registration/register.html', {'form':form})



def confirm_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            profile = Profile.objects.get(confirmation_code=code)
            profile.is_confirmed = True
            profile.save()

            user = profile.user
            login(request, user)

            return redirect('autho_app:index')
        
        except Profile.DoesNotExist:
            error = "The code is incorrect. Please check it again."
            return render(request, 'registration/confirm_email.html', {'error': error})
        
    return render(request, 'registration/confirm_email.html')


class CustomLoginView(auth_views.LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'


# REST Framework
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer