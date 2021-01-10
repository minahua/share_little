from django.urls import path
from . import views

app_name='cms'
urlpatterns=[
    path('',views.htsy),
    path('login/',views.htdlym,name='login')
]