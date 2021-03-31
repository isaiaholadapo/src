from django.urls import path


from transaction.api.views import account_detail_view


app_name = 'transaction'

urlpatterns = [
    path('home', account_detail_view, name = 'home'),
    
]