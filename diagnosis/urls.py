from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('', views.home, name='home'),
    path('heart/', views.heart, name='heart'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('lung/', views.lung, name='lung'),
    path('kidney/', views.kidney, name='kidney'),
    path('thyroid/', views.thyroid, name='thyroid'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
