# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
import feedparser
import logging
import sys
sys.path.append("/Users/saravananveeramani/Coding/pythonprj/mysite")
import common as config


# Create your views here.
feeds = config.GetParseResults(config.business_urls)

def index(request):
    return render(request,'personal/home.html',{'test':feeds})
