from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def maiscula_m2(value):
    lista = value.split(' ')
    lista = [w.capitalize() if w not in ['dos','da','de', 'do'] else w for w in lista]
    return ' '.join(lista)