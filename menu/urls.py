from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.food_list_view, name='food_list'),
    path('vote/<int:food_id>/', views.vote_view, name='vote'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]