from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from django.template.defaultfilters import slugify


def index(request):
    return render(request, 'blog/index.html',
                  {
                      'latest_blog_list': Blog.objects.order_by('-posted')[:5],
                      'category_list': Category.objects.all()
                  })


def blog_detail(request, slug):
    blog_item = get_object_or_404(Blog, slug=slug)
    return render(request,
        'blog/detail.html',
        {
            'blog': blog_item,
            'category': blog_item.category,
            'category_list': Category.objects.all(),
        })


def category(request, slug):
    category_item = get_object_or_404(Category, slug=slug)
    return render(request,
        'blog/category.html',
        {
            'category': category_item,
            'category_list': Category.objects.all(),
            'blog_list': Blog.objects.filter(category=category_item)
        })


@login_required()
def create_blog(request):
    context = {
            'category_list': Category.objects.all(),
        }
    return render(request, 'blog/create_blog.html', context)


@login_required()
def edit_blog(request, slug):
    blog_item = get_object_or_404(Blog, slug=slug)
    context = {
            'blog': blog_item,
            'category': blog_item.category,
            'category_list': Category.objects.all(),
        }
    return render(request, 'blog/edit_blog.html', context)


def create_or_update_blog(request, slug=None):
    if slug:
        blog_item = get_object_or_404(Blog, slug=slug)
    else:
        blog_item = Blog()

    blog_item.title = request.POST['blog_title']
    if not blog_item.slug:
        blog_item.slug = slugify(blog_item.title)

    blog_item.body = request.POST['blog_body']
    cat = get_object_or_404(Category, slug=request.POST['blog_category'])
    blog_item.category = cat
    blog_item.save()
    return blog_item

@login_required()
def save_new_blog(request):
    blog_item = create_or_update_blog(request)

    return HttpResponseRedirect(reverse('blog:detail', args=(blog_item.slug,)))


@login_required()
def update_existing_blog(request, slug):
    blog_item = create_or_update_blog(request, slug=slug)

    return HttpResponseRedirect(reverse('blog:detail', args=(blog_item.slug,)))



