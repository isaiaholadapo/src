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
from django.conf import settings
from django.conf.urls.static import static

from account.views import (
    home_view,
    about_view,
    service_view,
    contact_view,
    registration_view,
    login_view,
    logout_view,
)

from transaction.views import (
    account_view,
    deposit_view,
    withdraw_view, 
    transfer_view,
    transaction_view,
    deposit_search_view,
    withdraw_history_view,
    deposit_history_view,
    transfer_history_view,
    
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('about/', about_view, name = 'about'),
    path('service/', service_view, name = 'service'),
    path('contact/', contact_view, name = 'contact'),
    path('account-details/', account_view, name = 'account-details'),
    path('register/', registration_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/',  logout_view, name = 'logout'),
    path('deposit/',  deposit_view, name = 'deposit'),
    path('withdraw/',  withdraw_view, name = 'withdraw'),
    path('transfer/',  transfer_view, name = 'transfer'),
    path('transaction/',  transaction_view, name = 'transaction'),
    path('dte/', deposit_search_view, name = 'dte'),
    path('withdraw-history/', withdraw_history_view, name = 'withdraw-history'),
    path('deposit-history/', deposit_history_view, name = 'deposit-history'),
    path('transfer-history/', transfer_history_view, name = 'transfer-history'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
