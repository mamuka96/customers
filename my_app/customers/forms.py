from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from .models import Professions, Customers
from django.contrib.auth.models import User

class CustomersForm(forms.ModelForm):

    class Meta():
        model = Customers
        fields = {'first_name', 'second_name', 'birthdate', 'salary', 'professions', }



class ProfessionsForm(forms.ModelForm):

    class Meta():
        model = Professions
        fields = {'profession_name', }


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta(User):
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2',
        }


class LoginForm(AuthenticationForm):

    email = forms.CharField()
    password = forms.CharField()


class ResetPasswordForm(forms.Form):

    email = forms.EmailField()

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()
