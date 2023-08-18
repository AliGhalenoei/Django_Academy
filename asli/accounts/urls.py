from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('singup/',views.SingupView.as_view(),name='singup'),
    path('veryfy/',views.VeryfyView.as_view(),name='veryfy'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('password_reset/',views.UserPassword_ResetView.as_view(),name='password_reset'),
    path('password_reset_done/',views.UserPassword_Reset_DoneView.as_view(),name='password_reset_done'),
    path('password_reset_done/<uidb64>/<token>/',views.UserPassword_Reset_ConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',views.UserPassword_Reset_CompleteView.as_view(),name='password_reset_complete'),
    path('user_profile/<int:pk>/',views.UserProfileView.as_view(),name='user_profile'),
    # Api..
    path('login_api/',views.LoginAPIView.as_view(),name='login_api'),
    path('singup_api/',views.SingupAPIView.as_view(),name='singup_api'),
    path('logout_api/',views.LogoutAPIView.as_view(),name='logout_api'),
    # CRUD Users...
    path('list_user_api/',views.ListUserAPIView.as_view(),name='list_user_api'),
    path('rud_user_api/<int:pk>/',views.RUD_UserAPIView.as_view(),name='rud_user_api'),
]
