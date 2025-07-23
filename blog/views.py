from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect


def blog_index(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return render(request, "blog/all-posts.html")


def post_detail (request, slug):
    return render(request, "blog/post-detail.html")