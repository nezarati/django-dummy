from django.urls import path
from . import views

app_name = "business_profile"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
]
