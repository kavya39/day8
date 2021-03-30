from django.urls import path
from team import views

urlpatterns = [
path('',views.hello),
path('demo/',views.chk),
path('hm/',views.home),
path('lg/',views.lgn),
path('rg/',views.reg)
]
