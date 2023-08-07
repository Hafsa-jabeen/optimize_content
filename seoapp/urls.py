from django.urls import path
from . import views

app_name = "seoapp"
urlpatterns = [
    path("", views.index, name="index"),
    path('optimize/', views.optimize, name='optimize'),
]