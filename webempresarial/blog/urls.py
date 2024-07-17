from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="detail_blog"),
    path("create/", views.BlogCreateView.as_view(), name="create_blog"),
    path("update/<int:pk>/", views.BlogUpdateView.as_view(), name="update_blog"),
    path("delete/<int:pk>/", views.BlogDeleteView.as_view(), name="delete_blog"),
    ### CATEGORÍAS
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="create_category"),
    path("categories/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="update_category"),
    path("categories/delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete_category"),
]
