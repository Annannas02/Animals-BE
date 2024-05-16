from django.urls import path
from animals import views


urlpatterns = [
    path('', views.AnimalList.as_view()),
    path('<int:pk>/', views.AnimalDetail.as_view()),  # Add this line
]