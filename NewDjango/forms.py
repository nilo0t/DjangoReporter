from django import forms
from django.contrib.auth import get_user_model

user=get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your full name"}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "enter your message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "login__input", "placeholder":" UserName-Email"})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"class": "login__input", "placeholder":"Password"})
    )


class RegisterForm(forms.Form):
    fullName = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "login__input","placeholder": "FullName"})
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={"class": "login__input", "placeholder": "UserName-Email"}))

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"class": "login__input", "placeholder": "Password"})
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"class": "login__input", "placeholder": "Confirm-Password"})
    )

    def clean_fullName(self):
        fullName = self.cleaned_data.get("fullName")
        qs = user.objects.filter(username=fullName)
        if qs.exists():
            raise forms.ValidationError("FullName is Taken")
        return fullName

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is Taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return data
