from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    # UpdateViews
    path("update/coreone/<int:pk>/", views.HomeCoreOneUpdateView.as_view(), name="core_one"),
    path("update/coretwo/<int:pk>/", views.HomeCoreTwoUpdateView.as_view(), name="core_two"),
]
