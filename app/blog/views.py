from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http import HttpResponseRedirect

from .forms import LoginForm, RegisterForm


def login_view(request):

    if request.method == "POST":
        # create form with request.POST data.
        form = LoginForm(request.POST)

        if form.is_valid():
            # get the cleaned form data, in this case just the username and password.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                raise ValidationError("Invalid username or password.")
    else:
        # if request.method is not POST, just create a Form without any data.
        form = LoginForm()

    return render(request, "auth.html", context=dict(form=form, title="Sign in"))


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            # getting the cleaned form data.
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["repeat_password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            if not confirm_password:
                # if the password is not repeated, raise an Error.
                raise ValidationError("You need to confirm your password.")
            if password != confirm_password:
                # if the passwords do not match, raise an Error.
                raise ValidationError("Passwords do not match.")

            # at this point we're assuming there's nothing wrong with the values supplied by the user.
            # so we want to create a new user with given username, password etc.
            new_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            # save the new user object.
            new_user.save()
            # authenticate the user so we can immediately log in the user.
            user = authenticate(request, username=username, password=password)
            # self-explanatory.
            login(request, user)

    else:
        form = RegisterForm()

    return render(request, "auth.html", context=dict(form=form, title="Register"))
