from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.core.mail import send_mail
from .models import Profile



def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)

            # Sending message with the code
            send_mail(
                'Registration confirmation',
                f'Your confirmation code: {profile.confirmation_code}',
                'alserikbolov@mail.ru',
                [user.email],
                fail_silently=False,
            )
            return redirect('accounts:confirm_email')
    else:
        form = CreateUserForm()
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)



# Processing verification code
"""The code from the form is checked, if it exists and matches, 
the profile is confirmed and the user is redirected to the main page.
If the code is incorrect, the user is shown an error"""

def confirm_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            profile = Profile.objects.get(confirmation_code=code)
            profile.is_confirmed = True
            profile.save()
            return redirect('accounts:login')
        except Profile.DoesNotExist:
            error = "The code is incorrect. Check it again."
            return render(request, 'registration/confirm_email.html', {'error': error})
        
    return render(request, 'registration/confirm_email.html')