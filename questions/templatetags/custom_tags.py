
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag
def active_url(request, url_name):
    try:
        url = reverse(url_name)
    except NoReverseMatch:
        return 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
    
    if request.path == url:
        return 'border-indigo-500 text-gray-900'
    return 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'




@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})
