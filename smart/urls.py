"""smartGrocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from fridge import views as user_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('fridge.urls')),
    url(r'^signup$',user_views.register,name='register'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'profile/$', user_views.profile, name='profile'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    # urlpatterns = patterns('',
    # url(r'^shopping-cart/', include('shopping.urls')),
# )
]

