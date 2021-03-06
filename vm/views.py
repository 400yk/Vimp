import json
import pytz
from math import *
from sum_votes import sum_votes
from django.shortcuts import render, render_to_response, get_object_or_404
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from vm.models import Wasco, Precinct
from vm.forms import VoteResponseForm

def home(request):
    context = RequestContext(request)
    return render_to_response('vm/home.html', context)

def getColor(value):
    red = 0
    blue = 0
    green = 0
    if (value > 1):
        trimmed_value = min(value, 3)
        red = 255
        blue = round((1 - trimmed_value / 3) * 255)
        green = round((1 - trimmed_value / 3) * 255)
        trimmed_value = None
    elif (value == 1):
        return "#FFFFFF"
    elif (value < 1):
        trimmed_value = 1 / value
        trimmed_value = min(trimmed_value, 3)
        blue = 255
        red = round((1 - trimmed_value / 3) * 255)
        green = round((1 - trimmed_value / 3) * 255)
        trimmed_value = None

    second = red % 16
    first = (red - second) / 16
    fourth = green % 16
    third = (green - fourth) / 16
    sixth = blue % 16
    fifth = (blue - sixth) / 16
    return ("#" + hex(int(first))[2:].upper() + hex(int(second))[2:].upper() + hex(int(third))[2:].upper() + hex(int(fourth))[2:].upper() + hex(int(fifth))[2:].upper() + hex(int(sixth))[2:].upper())

def home_precinct_list(request):
    context = RequestContext(request)
    precinct_obj = []
    if request.method == "GET":
        precinct_obj = request.GET['precinct_list']
        if precinct_obj:
            precinct_obj = json.loads(precinct_obj)

            # Check if any precinct isn't in the database, if not insert one
            try:
                Precinct.objects.get(pk = precinct_obj['name'])
            except Precinct.DoesNotExist:
                p = Precinct.objects.create(
                        name = precinct_obj['name'],
                        coord_lat = precinct_obj['coord_lat'],
                        coord_lng = precinct_obj['coord_lng'],
                        coord_alt = precinct_obj['coord_alt'],
                        area = precinct_obj['area'],
                        count_yes = 0,
                        count_no = 0,
                        count_undecided = 0,
                        count_yardsign = 0
                        )
                p.save()

    # If didn't pass in a list of precincts, use the default 
        # list from the database, this happens when user first 
        # loads the home page (without uploading own precinct file)
        #else:
        #    precinct_objs = Precinct.objects.all()

    return render_to_response('vm/home_precinct_list.html', {'precinct_objs': precinct_obj}, context)

def home_precinct_list_default(request):
    context = RequestContext(request)
    precinct_list_default = Precinct.objects.all()
    list_precinct = '['
    list_precinct_dict = []
    for precinct in precinct_list_default:
        precinct_dict = {'name': precinct.name,
                'coord_alt': precinct.coord_alt,
                'coord_lat': precinct.coord_lat,
                'coord_lng': precinct.coord_lng,
                'yardsign': precinct.count_yardsign,
                'vote_yes': precinct.count_yes,
                'vote_no': precinct.count_no,
                'undecided': precinct.count_undecided,
                'color': getColor((precinct.count_yes + 0.001) / (precinct.count_no + 0.001))
                }
        list_precinct_dict.append(precinct_dict)
        list_precinct += json.dumps(precinct_dict) + ','
    # Delete the last comma
    list_precinct = list_precinct[:-1]
    list_precinct += ']'
    rendered_html = render_to_response('vm/home_precinct_list.html', {'precinct_objs': list_precinct_dict}, context)
    return HttpResponse(json.dumps({
        "list_precinct": list_precinct,
        "rendered_html": rendered_html.content}), content_type="application/json")

def precinct_detail(request, precinct_name):
    context = RequestContext(request)
    voters = None
    if precinct_name:
        # Remove the leading zeros in the name string
        precinct_name = int(precinct_name.lstrip("0"))
        voters = Wasco.objects.filter(sprecinctid__exact = precinct_name)

    return render_to_response('vm/precinct_detail.html', {'voters': voters}, context)

def voter_response(request, voter_id):
    context = RequestContext(request)
    if request.method == "POST":
        if voter_id:
            voter = get_object_or_404(Wasco, pk = voter_id)
            form = VoteResponseForm(request.POST, instance = voter)

        if form.is_valid():
            response_record = form.save(commit = False)
            response_record.time_response = datetime.now(pytz.timezone('US/Pacific'))
            response_record.save()
            sum_votes()
        else:
            print form.errors
    elif request.method == "GET":
        if voter_id:
            voter = Wasco.objects.get(pk = voter_id)
            form = VoteResponseForm(instance = voter)

    return render_to_response("vm/voter_response.html", {'form': form, 'voter': voter}, context)
