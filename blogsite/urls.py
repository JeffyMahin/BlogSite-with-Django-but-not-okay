from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='status_details'),
]
