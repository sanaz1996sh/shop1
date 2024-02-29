from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    # List view (Read all)
    path('product/', productList.as_view()),

    # Create view
    path('product/create/',productList.as_view()),

    #update view
    path('product/update/',productList.as_view()),

    #delete
    path('product/delete/',productList.as_view()),

    # Retrieve view (Read one)
    path('product/<adad>/',productRetrieveView.as_view()),

    path('login/',views.obtain_auth_token),

    











    # Create view
    #path('product/create/', views.productCreateView.as_view(), name='product-create'),

    # Retrieve view (Read one)
    #path('product/<int:pk>/', views.productRetrieveView.as_view(), name='product-retrieve'),

    # Update view
    #path('product/<int:pk>/update/', views.productUpdateView.as_view(), name='product-update'),

    # Delete view
    #path('product/<int:pk>/delete/', views.productDeleteView.as_view(), name='product-destroy'),

]