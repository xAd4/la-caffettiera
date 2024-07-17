from django.urls import path
from . import views

urlpatterns = [
    path("", views.AboutTemplateView.as_view(), name="about"),
    path("update/<int:pk>/", views.AboutUpdateView.as_view(), name="update_about"),
]
