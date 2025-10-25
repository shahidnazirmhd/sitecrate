from django.urls import path


from . import views


urlpatterns = [
    path("", views.BlogIndexView.as_view(), name="blog-index"),
    path("posts/", views.AllPostsView.as_view(), name="blog-all-posts"),
    path("posts/<slug:slug>/", views.DetailPostView.as_view(), name="blog-post-detail"),
]