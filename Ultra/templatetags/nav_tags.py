from django import template
from django.core import urlresolvers

register = template.Library()

@register.simple_tag
def navactive(request, views):
    views = [str(view) for view in views.split()]
    try:
        view = urlresolvers.resolve(request.path).url_name
        print view

        if view in views:
            return "active"
        else:
            return ""
    except urlresolvers.Resolver404:
        return ""
