from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from accounts.models import Profile
User= get_user_model()

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'First Name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','minlength':'10','maxlength':'40','placeholder':'Email Address'}))  
       
    class Meta:
        model = User
        fields =('first_name','last_name','email','password1','password2')
           
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already taken")
        return email   
    
    
    
class LoginForm(forms.ModelForm):
    password = forms.CharField(
        
                               widget=forms.PasswordInput
                               (attrs={'placeholder':'Enter your Password','class':'form-control'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email address','class':'form-control'}))
 
    class Meta:
        model = User
        fields= ('email', 'password')
        def clean(self):
            if(self.is_valid)():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email,password=password):
                    raise forms.ValidationError('Invalid credentials')
     
       
class ProfilePageForm(forms.ModelForm):
    address1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter address line 1',}))  
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter address line 2',}))  
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter postal code',}))  
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter city',}))  
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter state',})) 
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter first name',}))  
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter last name',})) 
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'enter country',})) 
    class Meta:
      model =Profile
      fields = ('address1', 'address2','country','city','state','zipcode','first_name','last_name',)
                 