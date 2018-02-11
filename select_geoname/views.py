# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.http import JsonResponse

import cities

# Create your views here.

def where_are_you(request):
    context = {}
    countries = cities.models.Country.objects.all()

    response = {"status": False, "errors": []}

    if request.is_ajax() and request.GET['action']=="for_states":
        country_id = request.GET['country_id']
        country = cities.models.Country.objects.get(id=country_id)
        if country:
            states = cities.models.Region.objects.filter(country=country)
            context.update({
                "states":states,
            })
            template = render_to_string("select_geoname/get_states.html", context)
            response = {"data": template}
            return HttpResponse(json.dumps(response), content_type="application/json")

    if request.is_ajax() and request.GET['action']=="for_cities":
        state_id = request.GET['state_id']
        state = cities.models.Region.objects.get(id=state_id)
        if state:
            citys = cities.models.City.objects.filter(region=state)
            context.update({
                "cities":citys,
            })
            template = render_to_string("select_geoname/get_cities.html", context)
            response = {"data": template}
            return HttpResponse(json.dumps(response), content_type="application/json")

    if request.is_ajax() and request.GET['action']=="form_submit":
        form_data = request.GET["form_data"]
        country_id = request.GET["country"]
        state_id = request.GET["state"]
        city_id =  request.GET["city"]

        city = cities.models.City.objects.filter(id=city_id).first()
        country = cities.models.Country.objects.filter(id=country_id).first()
        state = cities.models.Region.objects.filter(id=state_id).first()

        data={
            "city_name":city.name,
            "country_name":country.name,
            "state_name":state.name
        }
        return JsonResponse(data)

    context.update({
        "countries":countries,
    })

    return render(request, "select_geoname/where_are_you.html", context)
