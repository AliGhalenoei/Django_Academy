from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import views as auth_view
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.backends import ModelBackend
import random
# .imports..
from .models import *
from .forms import *
from utils import Send_Otp_Code
from .serializers import *

# DRF imports...
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.

class LoginView(View):
    form_class=LoginForm
    template_name='accounts/login.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(
                phone=cd['phone'],
                password=cd['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,self.template_name,{'fomr':form})
    
class SingupView(View):
    form_class=SingupForm
    template_name='accounts/singup.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            create_code_random=random.randint(1000,9999)
            Send_Otp_Code(cd['phone'],create_code_random)
            OTP.objects.create(phone=cd['phone'],code=create_code_random)
            request.session['singup_info']={
                'phone':cd['phone'],
                'email':cd['email'],
                'password':cd['password'],
            }
            return redirect('veryfy')
        return render(request,self.template_name,{'form':form})
    
class VeryfyView(View):
    form_class=VeryfySingupForm
    template_name='accounts/veryfy.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request):
        user_session=request.session['singup_info']
        get_code=OTP.objects.get(phone=user_session['phone'])
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if cd['code'] == get_code.code:
                User.objects.create_user(
                    phone=user_session['phone'],
                    email=user_session['email'],
                    password=user_session['password'],
                )
                get_code.delete()
                return redirect('login')
        return render(request,self.template_name,{'form':form})
    
# class EmailBackend(ModelBackend):
#     def authenticate(self,request,phone=None,password=None,email=None,**kwargs):
#        if phone:
#            try:
#                user=User.objects.get(phone=phone)
#            except User.DoesNotExist:
#                 return None
#        elif email:
#             try:
#                user=User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return None
#        else:
#            return None
       
#        if user.check_password(password):
#            return user
#        return None
    
    # def get_user(self,pk):
    #     try:
    #         return User.objects.get(id=pk)
    #     except User.DoesNotExist:
    #         return None

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
    
class UserPassword_ResetView(auth_view.PasswordResetView):
    template_name='accounts/password_reset_form.html'
    success_url=reverse_lazy('password_reset_done')
    email_template_name='accounts/password_reset_email.html'

class UserPassword_Reset_DoneView(auth_view.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class UserPassword_Reset_ConfirmView(auth_view.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    success_url=reverse_lazy('password_reset_complete')

class UserPassword_Reset_CompleteView(auth_view.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'

class UserProfileView(View):
    template_name='accounts/user_profile.html'

    def get(self,request,pk):
        user=UserProfile.objects.get(id=pk)
        return render(request,self.template_name,{'user':user})
    
# Django DRF...

class LoginAPIView(APIView):

    def post(self,request):
        srz_data=LoginSerializer(data=request.POST)
        if srz_data.is_valid():
            vd=srz_data.validated_data
            user=authenticate(
                phone=vd['phone'],
                password=vd['password']
            )
            if user is not None:
                login(request,user)
                return Response({'massage':'User Logined...'})
        return Response(data=srz_data.errors)

class SingupAPIView(APIView):

    def post(self,request):
        srz_data=SingupSerializer(data=request.POST)
        if srz_data.is_valid():
            vd=srz_data.validated_data
            User.objects.create_user(
                phone=vd['phone'],
                email=vd['email'],
                password=vd['password'],
            )
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)
    
class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return Response({'massage':'logouted..'})
    
class ListUserAPIView(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class RUD_UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    

    
    
    




