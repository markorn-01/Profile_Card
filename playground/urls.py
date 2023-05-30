from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduce),
    # path('experience/', views.show_experience)
]