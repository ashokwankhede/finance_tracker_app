from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.create_user, name='sign-up'),
    path('', views.sign_in, name='sign_in'),
    path('home/<str:username>', views.home, name='home'),
    path('create-transaction/<str:username>', views.create_transaction, name='create-transaction'),
]