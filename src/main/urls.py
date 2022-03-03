from django.urls import path
from .views import home_view,console_view


app_name = 'ips'
urlpatterns = [
path('',home_view),
path('console/',console_view),

]