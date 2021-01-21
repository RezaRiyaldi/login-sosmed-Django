from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.home, name = 'home'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
]
