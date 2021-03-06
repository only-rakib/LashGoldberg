from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('law_firm/', views.law_firm_view, name='law_firm'),

    path('practices/', views.practice_view, name='practices'),
    path('practices/<slug:slug>', views.practice_inside_view, name='practices_inside'),

    path('attorneys/', views.attorneys_view, name='attorneys'),
    path('offices/', views.offices_view, name='offices'),
    path('offices/<str:office_title>-<int:pk>',
         views.offices_inside_view, name='offices_inside'),
    path('disclaimer/', views.disclaimer_view, name='disclaimer'),
    path('sitemap/', views.sitemap_view, name='sitemap'),
    path('blog/', views.blog_view, name='blog'),
    path('inside_practice/', views.inside_practice_view, name='inside_practice'),
    path('inside_team/', views.inside_our_team_view, name='inside_team'),

]
