from django import template
from contact.models import AboutModel, ContactLink


register = template.Library()


@register.simple_tag()
def get_about():
    """Вывод about"""
    return AboutModel.objects.last()


@register.inclusion_tag('contact/include/tags/social_links.html')
def get_social_links():
    links = ContactLink.objects.all()
    return {"contact_links": links}


@register.inclusion_tag('contact/include/tags/social_links_only_url.html')
def get_social_links_only_url():
    links = ContactLink.objects.all()
    return {"contact_links_only_url": links}