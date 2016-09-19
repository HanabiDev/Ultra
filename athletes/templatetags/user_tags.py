from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

from urllib import urlencode
from urllib2 import urlopen

register = template.Library()


@register.simple_tag
def bitlyfy(the_url):
    ACCESS_KEY = '6bd025953bb34dcf1867b8bfedb2bdd6ab1f36c4'
    endpoint = 'https://api-ssl.bitly.com/v3/shorten?'
    t = urlencode({'access_token':ACCESS_KEY, 'longUrl':the_url})
    cas = endpoint+t+"&format=txt"
    print urlopen(cas).read()
    return urlopen(cas).read()


@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

