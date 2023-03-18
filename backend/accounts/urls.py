from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts import views as accounts_views
from . import views



urlpatterns = [
    path('findpassword/',accounts_views.change_password),
    path('findemail/', accounts_views.ForgotEmailView),
    path('create/', accounts_views.createUser),
    path('login/', accounts_views.login),
    path('logout/', accounts_views.logout),
    path('userlist/',accounts_views.userlist),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]