from django import template
from operational_service import *

register = template.Library()

@register.filter
def check_service(service_name):
    if service_name == "Firewall":
        return check_service_firewall()
    if service_name == "Database":
        return check_database_connection()
