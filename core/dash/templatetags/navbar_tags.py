from django import template
from dash.models import Navbar


register = template.Library()
navbar_list = Navbar.objects.all()


@register.filter(name='get_navbar_title')
def get_navbar_title(get_navbar_title):
    for item in navbar_list:
        if (item.btn_name in get_navbar_title):
            return item.title
