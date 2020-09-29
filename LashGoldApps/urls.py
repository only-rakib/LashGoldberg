from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('law_firm/', views.law_firm_view, name='law_firm'),

]
