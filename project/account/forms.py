from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
# from account.models import User
from django.contrib.auth.models import User
# #########################################################################
# ## ClassName  : LoginForm
#    Input      : Username and Password
#    Output     : Display username and password fields on the login screen
#    Usage     : Login Screen
# #########################################################################

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=True, max_length=30,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'name': 'username'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                           widget=forms.PasswordInput(attrs={
                               'class': 'form-control',
                               'name': 'password'}))

# #####################################################################################
# ## ClassName  : SignUpForm
#    Input      : Username, first_name, last_name, email, country, password1, password2
#    Output     : Display all input fields on signup form
#    Usage     : Signup Screen
# #####################################################################################
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username*  ",max_length=30, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'name': 'username'}))
    first_name = forms.CharField(label="First name*  ",max_length=30, required=True,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'name': 'first_name'}))
    last_name = forms.CharField(label="Last name*  ",max_length=30, required=True,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'name': 'last_name'}))
    email = forms.EmailField(label="Email*  ",max_length=254,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'name': 'email','type':'email'}))

    password1 = forms.CharField(max_length=254,label="password*  ",
                             widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'name': 'password1'}))
    password2 = forms.CharField(max_length=254, label=" Confirm password*  ",
                             widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'name': 'password2'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')