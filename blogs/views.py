from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Blog


def blog_index_page(request: HttpRequest) -> HttpResponse:
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 9)
    page_number = request.GET.get("page")
    blogslist = paginator.get_page(page_number)
    print(blogslist)
    return render(request, "blogs/index.html", {"blogslist": blogslist})


def blog_detail_page(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Get the next and previous blog posts
    next_blog = (
        Blog.objects.filter(pub_date__gt=blog.pub_date).order_by("pub_date").first()
    )
    prev_blog = (
        Blog.objects.filter(pub_date__lt=blog.pub_date).order_by("-pub_date").first()
    )

    # Get more blogs for the "More Blogs" section
    more_blogs = Blog.objects.exclude(id=blog.id).order_by("-pub_date")[:4]

    context = {
        "blog": blog,
        "next_blog": next_blog,
        "prev_blog": prev_blog,
        "more_blogs": more_blogs,
    }
    return render(request, "blogs/blog-detail.html", context)
