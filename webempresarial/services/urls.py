from django.urls import path
from . import views

urlpatterns = [
    path("", views.ServiceListView.as_view(), name="services"),
    path("create/", views.ServiceCreateView.as_view(), name="create_service"),
    path("update/<int:pk>/", views.ServiceUpdateView.as_view(), name="update_service"),
    path("delete/<int:pk>/", views.ServiceDeleteView.as_view(), name="delete_service"),
]

