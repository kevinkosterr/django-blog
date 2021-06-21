from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"placeholder": "johndoe", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "******", "class": "form-control"}
        ),
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs={"placeholder": "John", "class": "form-control"}),
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs={"placeholder": "Doe", "class": "form-control"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"placeholder": "johndoe@example.com", "class": "form-control"}
        ),
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"placeholder": "johndoe", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "******", "class": "form-control"}
        ),
    )
    repeat_password = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "******", "class": "form-control"}
        ),
    )
