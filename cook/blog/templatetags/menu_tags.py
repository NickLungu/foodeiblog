from django import template
from django.db.models import Count

from blog.models import Category, Post

register = template.Library()


def get_all_categories():
    categories = Category.objects.annotate(q_count=Count('post')).filter(q_count__gt=0) \
                                 .order_by('-q_count')[:4]
    return categories


def get_all_posts(a, b):
    posts = Post.objects.order_by('-id')[a:b]
    return posts


@register.simple_tag()
def get_list_categories():
    return get_all_categories()


@register.simple_tag()
def get_list_posts(a, b):
    return get_all_posts(a, b)


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    categories = Category.objects.all()
    # categories = Category.objects.filter(parent__isnull=True).order_by("name")
    return {"list_category": categories}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    # categories = Category.objects.filter(parent__isnull=True).order_by("name")
    return {"list_last_post": posts}