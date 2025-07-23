from django.urls import path


from . import views


urlpatterns = [
    path("", views.blog_index, name="blog-index"),
    path("posts/", views.all_posts, name="blog-all-posts"),
    path("posts/<slug:slug>/", views.post_detail, name="blog-post-detail"),
]