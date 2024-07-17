from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactTemplateView.as_view(), name="contact"),
    path("update/<int:pk>/", views.ContactUpdateView.as_view(), name="update_contact"),
]
