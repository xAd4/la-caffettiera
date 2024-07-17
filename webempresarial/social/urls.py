from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.SocialCreateView.as_view(), name="create_social"),
    path("update/<int:pk>/", views.SocialUpdateView.as_view(), name="update_social"),
    path("delete/<int:pk>/", views.SocialDeleteView.as_view(), name="delete_social"),
]
