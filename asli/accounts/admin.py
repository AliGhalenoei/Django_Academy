from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCrationForm

    fieldsets=(
        (None,{'fields':('phone','email','password')}),
        ('Status',{'fields':('is_admin','is_active')}),
        ('Permission',{'fields':('last_login',)}),
    )

    add_fieldsets=(
        (None,{'fields':('phone','email','password','password2')}),
    )

    list_display=('phone','email','is_admin')
    list_filter=('is_active',)
    search_fields=('email',)
    filter_horizontal=()
    ordering=('email',)

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)

admin.site.register(OTP)
admin.site.register(UserProfile)
