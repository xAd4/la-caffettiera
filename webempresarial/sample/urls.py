from django.urls import path
from . import views

urlpatterns = [
    path("", views.SampleListView.as_view(), name="sample"),
    path("detail/<int:pk>/", views.SampleDetailView.as_view(), name="detail_sample"),
    path("create/", views.SampleCreateView.as_view(), name="create_sample"),
    path("update/<int:pk>/", views.SampleUpdateView.as_view(), name="update_sample"),
    path("delete/<int:pk>/", views.SampleDeleteView.as_view(), name="delete_sample"),
]
