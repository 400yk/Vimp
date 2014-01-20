import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from vm.models import Wasco

def home(request):
    context = RequestContext(request)
    return render_to_response('vm/home.html', context)

def home_precinct_list(request):
    context = RequestContext(request)
    precinct_objs = []
    if request.method == "GET":
        precinct_objs = request.GET['precinct_list']
        precinct_objs = json.loads(precinct_objs)
            
    return render_to_response('vm/home_precinct_list.html', {'precinct_objs': precinct_objs}, context)

def precinct_detail(request, precinct_name):
    context = RequestContext(request)
    voters = None
    if precinct_name:
        # Remove the leading zeros in the name string
        precinct_name = int(precinct_name.lstrip("0"))
        voters = Wasco.objects.filter(sprecinctid__exact = precinct_name)
            
    return render_to_response('vm/precinct_detail.html', {'voters': voters}, context)
