from django.urls import path
from testapp import views 
urlpatterns=[
    path('show/',views.showIndex),
    path('data/',views.showData),
]