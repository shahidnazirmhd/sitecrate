from datetime import date

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from .models import Post


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


class DetailPostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
    

