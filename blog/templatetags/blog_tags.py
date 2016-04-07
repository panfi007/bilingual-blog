from django import template
register = template.Library()
from ..models import Post
from django.utils.safestring import mark_safe
import markdown


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/slider.html')
def slider_latest_posts(count=5):
    slider_latest = Post.published.order_by('-publish')[:count]
    return {'slider_latest': slider_latest}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))