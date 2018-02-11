# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import cities

# Create your views here.

def where_are_you(request):
    context = {}
    countries = cities.models.Country.objects.all()
    print "countries++++++++++++++++++++++++++++++++"
    print countries


    citys = cities.models.City.objects.all()

    print "cities +++++++++++++++++++++++++"
    print citys


    region = cities.models.Region.objects.all()

    print "region +++++++++++++++++++++++++++++"
    print region

    context = {
        "countries":countries,
        "region":region,
        "citys":citys
    }

    return render(request, "select_geoname/where_are_you.html", context)
