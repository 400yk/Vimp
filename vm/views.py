import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

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
