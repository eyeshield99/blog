from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def blog_index_page(request: HttpRequest) -> HttpResponse:
    return render(request, "blogs/index.html")
