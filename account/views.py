from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    """Create a new login form for new users, checks if user already exists and active in database"""
    if request.method == 'POST':
        form = LoginForm(request.POST)  # instantiate form with submitted data
        if form.is_valid():  # checks if form is filled out properly
            cd = form.cleaned_data
            # if form has valid input, authenticate() checks request object, username object,
            # password object against database, if successful, outputs Authenticated successfully,
            # if not then becomes None object and outputs Invalid login
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:  # if authenticated successfully, checks if user is active in database
                    login(request, user)  # sets user in session by calling login
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')  # outputs if user is not active in database
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


