from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_index_page, name="blog-index"),
    path("<slug:slug>/", views.blog_detail_page, name="blog-detail"),
]
