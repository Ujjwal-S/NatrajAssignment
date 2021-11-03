from django.urls import path
from . import views


urlpatterns = [
    path('', views.VehicleListView.as_view(), name="home-page"),
    path('create/', views.VehicleCreateView.as_view(), name="vehicle-create"),
    path('<str:pk>/', views.VehicleDetailView.as_view(), name="vehicle-detail"),
    path('<str:pk>/update/', views.VehicleUpdateView.as_view(), name="vehicle-update"),
    path('<str:pk>/delete/', views.VehicleDeleteView.as_view(), name="vehicle-delete")
]