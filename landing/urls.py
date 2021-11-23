from django.urls import path
from .views import Landing, Login, Register, Logged_out, Logout_page, About

urlpatterns = [
    path('', Landing.as_view(), name="landing"),
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logged_out/', Logged_out.as_view(), name="logged_out"),
    path('logout_page/', Logout_page.as_view(), name="logout_page"),
    path('about/', About.as_view(), name="about"),
]