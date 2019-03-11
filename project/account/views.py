from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import NoReverseMatch, reverse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.views import login, logout
from account.forms import SignUpForm, LoginForm
from account.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.contrib import auth


# ########################################################
# ## FunctionName   : login_view
#    Input          : username and password
#    Output         : valid user only access entire site
#    Usage          : Login Screen
# ########################################################
def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    template = 'account/login.html'
    form = LoginForm
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password) # check valid user or not
        if user is not None:
            if user.is_active: # check user account is active/not
                login(request, user)
                messages.success(request, "You have logged in!")
                return redirect('/')
            else:
                messages.warning(request, "Your account is disabled!")
                return HttpResponseRedirect(reverse('login'))
        else:
            print('dddd')
            messages.warning(request, "The username or password are not valid!")
            return HttpResponseRedirect(reverse('login'))
    context = {'form': form, 'Title': 'Login'}
    return render(request, template, context)

# ########################################################
# ## FunctionName   : signup
#    Input          : Username, first_name, last_name, email, password1, password2
#    Output         : create new user
#    Usage          : Signup Screen
# ########################################################
def signup(request):
    status = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = status
            user.save()
            if status == False:  #IF ACTIVE STATUS FALSE IT WILL SEND MAIL TO THE USER TO ACTIVATE

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message) #MAIL SEND HERE
                return render(request, 'account/account_activation_sent.html', {'Title': 'Activate Account'})
            else:
                messages.success(request, "Your account is Created sucessfully..!")
                return redirect('login')
    else: # redirect signup form
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form, 'Title': 'Sign up'})


# ##########################################################
# ## FunctionName   : activate
#    Output         : Activate user account
#    Usage          : When click activation link form mail 
# ##########################################################
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token): # allow valid link
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Your Mail is verified and account is Created sucessfully..!")
        return redirect('login')
    else: # Invalid Link

        return render(request, 'account/account_activation_invalid.html',{'Title': 'Activate Account'})


# #############################################################
# ## FunctionName   : logout
#    Output         : redirect to home page
#    Usage          : Logout screen
# #############################################################
def logout(request):
    try:
        current_user = request.user
        auth.logout(request)
        return redirect('/')
    except User.DoesNotExist:
        return redirect('/')