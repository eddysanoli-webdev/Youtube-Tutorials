from django.shortcuts import render, redirect

# To make certain views only accesible while logged in
from django.contrib.auth.decorators import login_required

# Import flash messages (They dissapear after the next request)
# Types of message:
#   - messages.debug
#   - messages.info
#   - messages.success
#   - messages.warning
#   - messages.error
from django.contrib import messages

# Use pre-defined class for a User Creation form
from django.contrib.auth.forms import UserCreationForm

# Use custom form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# ==========================
# REGISTER VIEW
# ==========================

def register(request):

    # POST: Request to add a new user
    if request.method == "POST":

        # Pass the post request data to the user creation form
        # (If the form data is not valid, the following if statement wont execute
        # and the registration page will reload with the corresponding errors)
        form = UserRegisterForm(request.POST)

        # Validate the form data
        if form.is_valid():

            # Save the user to the database
            form.save()

            # Get the username from the form data
            username = form.cleaned_data.get('username')

            # Create success message
            messages.success(request, f'Your account has been created! You are now able to login')
            
            # Redirect back to the "login" page after Sign Up
            # (Blog-home is the alias given to the url pattern present in urls.py inside the blog app)
            return redirect('login')

    # GET (Or any other request): Display the user sign up page
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context ={
        'form': form
    })


# ==========================
# USER PROFILE VIEW
# ==========================

# Its necessary to add a decorator to require a login to access the login page
# (By default the decorator will redirect the user to "accounts/login". This can
# be changed inside the settings)

@login_required
def profile(request):

    # Get the update form for both the profile and the user
    user_update_form = UserUpdateForm()
    profile_update_form = ProfileUpdateForm()

    return render(request, 'users/profile.html', context = {
        'u_form': user_update_form,
        'p_form': profile_update_form
    })