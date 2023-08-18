from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manage import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    phone=models.CharField(max_length=11,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['email']

    objects=UserManager()

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class OTP(models.Model):
    phone=models.CharField(max_length=11)
    code=models.SmallIntegerField()

    def __str__(self) -> str:
        return str(self.code)
    
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profileuser')
    img=models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self) -> str:
        return str(self.user.id)

    
