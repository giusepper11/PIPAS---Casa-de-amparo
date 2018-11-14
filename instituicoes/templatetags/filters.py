from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

lista_stopwords = [
    'dos', 'da', 'de', 'do', 'em', 'e', 'pelo', 'com', 'a', 'das', 'pela'
]


@register.filter
@stringfilter
def maiscula_m2(value):
    lista = value.split(' ')
    lista = [w.capitalize() if w not in lista_stopwords else w for w in lista]
    return ' '.join(lista)
