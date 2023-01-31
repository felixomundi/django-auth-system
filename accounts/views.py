from django.shortcuts import render,redirect
from accounts.forms import UserRegistrationForm,LoginForm,ProfilePageForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from .tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str as force_text
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
UserModel = get_user_model()
     

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, f'{user} You are already logged in !!')
        return redirect('/')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           
            email=form.cleaned_data['email']
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data['last_name']
            user =(email,first_name, last_name)
            user = form.save(commit=False,)
            user.is_active = False            
            user.save()             
            profile = Profile.objects.create(user=user)                 
            messages.success(request, "Account created !! Please check your email to confirm your email address in order to activate your account.")
            # Welcome Email
            subject = "Welcome "+ user.first_name + " "+ user.last_name +" to Student Progress Mgt System"
            message = " Hello there,\n Welcome and thank you for signing up with us.\n Activate your account by clicking on the link that you will receive shortly"        
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = " Account Activation"
            message2 = render_to_string('accounts/emailconfirmation.html',{                
                'name': user.first_name +" "+ user.last_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user],
            )
            email.fail_silently = True
            email.send()
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request,error)
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,UserModel.DoesNotExist):
            user = None
    if user is not None and generate_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request,user)
        messages.success(request, "Your Account has been activated!!")
        return redirect('/')
    else:
        messages.error(request, 'Activation link is invalid')
    return redirect('/')

def loginuser(request):
    if request.user.is_authenticated:
        messages.warning(request, f' You are already logged in !!')
        return redirect('/')
    else:        
        if request.method == 'POST':            
            email = request.POST['email']
            password = request.POST['password']
           
            user = authenticate(request, email = email, password = password)
            if user is not None:
                form = login(request, user)                
                messages.success(request, f' welcome {email} !')
                path_redirect = request.get_full_path().split('?next=',1)
                if '?next=' in request.get_full_path():
                    return redirect(path_redirect[1])
                else:
                    return redirect('/')                     
                
            else:
                messages.error(request, f'Invalid details, please enter correct details or sign up!')
        form = LoginForm()       
    return render(request, 'accounts/login.html', {'form':form})


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, " Logged out successfully")
    return redirect('/')

@login_required(login_url='/accounts/login')    
def get_user_profile(request): 
    if request.method == 'POST':     
        profile_form = ProfilePageForm(request.POST,
                                       instance=request.user.profile)
        if profile_form.is_valid():
         
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
       
        profile_form = ProfilePageForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {'profile_form': profile_form,})
