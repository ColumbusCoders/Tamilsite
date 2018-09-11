# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import urllib2

response = urllib2.urlopen('http://business.dinamalar.com/news_details.asp?News_id=43247&cat=1')
html = response.read()
print html
# Create your tests here.
