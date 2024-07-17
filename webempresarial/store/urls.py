from django.urls import path
from . import views

urlpatterns = [
    path("", views.StoreTemplateView.as_view(), name="store"),
    path("update/<int:pk>/", views.StoreUpdateView.as_view(), name="update_store"),
]
