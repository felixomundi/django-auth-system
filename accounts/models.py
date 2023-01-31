from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from django.urls import reverse
from tinymce.models import HTMLField   
import uuid

class UserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Email address is required')
       
        if not first_name:
            raise ValueError("First Name required")
        if not last_name:
            raise ValueError("Last Name is required")
        user=self.model(
            email =self.normalize_email(email),
            first_name=first_name,
            last_name =last_name,
           
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,password:None):
        if not email:
            raise ValueError('Email address is required')
       
        if not first_name:
            raise ValueError("First Name required")
        if not last_name:
            raise ValueError("Last Name is required")
        user=self.model(
            email =self.normalize_email(email),           
             first_name=first_name,
            last_name =last_name,
            
        )
        user.set_password(password)
        user.is_admin =True
        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)    
    email =models.EmailField(verbose_name="email address",unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15) 
    is_admin = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)     
    is_student= models.BooleanField(default=False)
    is_parent= models.BooleanField(default=False)
    is_lecturer= models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)      
    date_registered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    last_login =models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True) 
    
    objects = UserManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ["first_name","last_name"]
    
    def __str__(self):
        return self.email
    def has_perm(self,perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    
class Profile(models.Model):
    id = models.UUIDField(
         primary_key = True,
        default = uuid.uuid4,
        editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)  
    address1 = models.CharField(max_length=200, null=False)
    address2 = models.CharField(max_length=200, null=False)
    country =  models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.email)
