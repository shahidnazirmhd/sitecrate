from datetime import date

from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect,  get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from .models import Post
from .forms import CommentForm


class BlogIndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-created_at"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
    

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-created_at"]
    context_object_name = "all_posts"


class DetailPostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            #return HttpResponseRedirect(reverse("blog-post-detail", args=[slug]))
            return redirect("blog-post-detail", slug=slug)
        
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)

