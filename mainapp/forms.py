from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from mainapp.models import Statuses, States
from django.core.exceptions import ValidationError
from fields import GetNameModelChoiceField, GetStateNameModelChoiceField, GetUnitModelChoiceField
from mainapp import util
from django.conf import settings
import requests
from django.db.models import Q
from django.core.validators import RegexValidator
import re
from django.contrib.auth import password_validation

User = get_user_model()

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'validate strongPassword','id':'new_password1'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'validate'}),
    )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    country_code = forms.CharField(max_length=30, required=False, help_text='Optional.')
    mobile_no = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # password1 = forms.CharField(max_length=30, required=False,validators=[util.alphabetChar])

    password1 = forms.CharField(required=False)
    password2 = forms.CharField(min_length=6,required=False)
    # city_name = forms.CharField(max_length=128, required=False)
    # state_id = forms.IntegerField(required=False)
    company_name = forms.CharField(max_length=64, required=False)
    # zipcode = forms.CharField(max_length=6, required=False)
    street_address = forms.CharField(max_length=128, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=254, label='', required=False,
                               widget=forms.TextInput(attrs={'style': 'display:none'}))

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'country_code', 'mobile_no', 'password1',
            'password2', 'company_name', 'street_address', 'email')

        def clean_display_name(self):
            mobile_no = self.cleaned_data['mobile_no']
            mobile_no
            if User.objects.filter(mobile_no=mobile_no).count() > 0:
                raise ValidationError('This Mobile Number is already in use.')
            return mobile_no


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'validate','autocomplete':'off'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'validate','autocomplete':'off'}))
    remember_me = forms.CharField(required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'filled-in', 'id': 'filled-in-box'}))

    class Meta:
        model = User
        fields = ('__all__')

    error_messages = {
        'invalid_login': "Password didn't match"
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        test = User.objects.filter(Q(email=username) | Q(mobile_no=username)).first()
        if not test :
            raise ValidationError("Invalid username or password.")
        elif(test.is_active ==0):
            raise ValidationError("Your account is deactivate.")
        else:
           return username

    def clean_username(self):
        username = self.cleaned_data['username']
        test = User.objects.filter(Q(email=username) | Q(mobile_no=username))
        if not test:
            raise ValidationError("Invalid username or password.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if (len(password) < 6):
            raise ValidationError("Password needs to be atleast 6 characters long")
            return password
        return password

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                self.add_error("password", "Password doesn't match")
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def clean_remember_me(self):

        remember_me1 = self.cleaned_data.get('remember_me')
        remember_me = str(remember_me1)
        if remember_me == 'False':
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        else:
            self.request.session.set_expiry(99560000)
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        return remember_me


class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=254, label='', widget=forms.TextInput(attrs={'class': 'validate','autocomplete':'off'}),
                               required=False)

    class Meta:
        model = User
        fields = ('username')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        checkEmail = self.validEmail(username)
        checkPhone = self.validPhone(username)
        checkNumber = self.all_numbers(username)
        if not (checkEmail | checkPhone):
            if checkNumber:
                raise ValidationError("Email/Phone no. doesn't exist.")
            else:
                raise ValidationError("Email/Phone no. doesn't exist.")
            raise ValidationError("Email/Phone no. doesn't exist.")
        try:
            user_found = User.objects.get(Q(email=username) | Q(mobile_no=username))
        except:
            user_found = None
        if not user_found:
            raise ValidationError("Email/Phone no. doesn't exist.")
        return username

    def validEmail(self, st):
        pattern = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        check = re.match(pattern, st)
        if check == None:
            return 0
        else:
            return 1

    def validPhone(self, st):
        pattern = re.compile("^[0-9]{10,10}$")
        check = re.match(pattern, st)
        if check == None:
            return 0
        else:
            return 1

    def all_numbers(self, st):
        pattern = re.compile("^[0-9]+$")
        check = re.match(pattern, st)
        if check == None:
            return 0
        else:
            return 1
