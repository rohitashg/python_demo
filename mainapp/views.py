# coding=utf-8
import base64

from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone

from mainapp import util
from mainapp.forms import SignUpForm

User = get_user_model()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def our_blog(request):
    return render(request, 'our_blog.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def python_user_signup(request):
    return render(request, 'contact_us.html')


@login_required()
def customer_profile(request):
    html = "<html><body>Web home page</body></html>"
    return HttpResponse(html)

def php_user_signup(request):
    if request.user.is_authenticated():
        return redirect('/home')
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'php_user_signup.html', {'form': form})

def confirm_email(request):
    """
    @this function create for email verification
    :param request:
    :return:
    """
    query_string = request.GET['id']
    user_id =  int(base64.urlsafe_b64decode(str(query_string)))
    user_object = User.objects.filter (id=user_id)
    user =  user_object[0]
    msg_txt = util.message_key[23]
    if user.email_verified == 1:
        msg_txt = util.message_key[24]
    else:
        update_data = dict()
        update_data['modified'] = timezone.now()
        update_data['email_verified'] = 1 # its means email is verfied
        user_object.update(**update_data)
    return render (request, 'confirm_email_success.html',{'msg': msg_txt})