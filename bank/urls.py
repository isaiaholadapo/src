"""bank URL Configuration

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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from account.views import (
    
    registration_view,
    login_view,
    logout_view,
)

from transaction.views import (
    home_view,
    deposit_view,
    withdraw_view
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('account-details/', home_view, name = 'home'),
    path('register/', registration_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/',  logout_view, name = 'logout'),
    path('deposit/',  deposit_view, name = 'deposit'),
    path('withdraw/',  withdraw_view, name = 'withdraw'),
]
