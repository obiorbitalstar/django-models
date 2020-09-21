from django.urls import path
from .views import HomeView,PostDetailView

urlpatterns = [ 

    path('home',HomeView.as_view(),name='home'),
    path('home/<int:pk>',PostDetailView.as_view(),name='post_details'),
    
    ]