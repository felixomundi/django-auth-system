from django.contrib import admin
from accounts.models import User,Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

class UserModelAdmin(admin.ModelAdmin):
    pass

class AdminUser(BaseUserAdmin):
    list_display=('email','last_login','is_active','is_student','is_parent','is_lecturer','is_admin','is_staff','is_superuser','date_registered','date_updated')
    search_fields=('email','last_login','is_active','is_student','is_parent','is_lecturer','is_admin','is_staff','is_superuser','date_registered','date_updated')
    readonly_fields=('date_registered','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()
    add_fieldsets=(
        (None,{
            'classes':('wide'),        
            'fields':('email','first_name','last_name','password1','password2'),
        }),
    )
    ordering= ('email',)
    
admin.site.register(User,AdminUser)    


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','country','created_at','updated_at')  
    ordering = ('-pk',)
    search_fields = ('user','country','created_at','updated_at')
