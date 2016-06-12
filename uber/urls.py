#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad
#
# Distributed under terms of the MIT license.

from django.conf.urls import url
from .views import get_availability

app_name = 'uber'
urlpatterns = [
    url(r'^availability/', get_availability),
]
