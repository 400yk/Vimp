import json
import pytz
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

def home_precinct_list(request):
    context = RequestContext(request)
    precinct_objs = []
    if request.method == "GET":
        precinct_objs = request.GET['precinct_list']
        if precinct_objs:
            precinct_objs = json.loads(precinct_objs)

            # Check if any precinct isn't in the database, if not insert one
            for obj in precinct_objs:
                # print obj['name']
                try:
                    Precinct.objects.get(pk = obj['name'])
                except Precinct.DoesNotExist:
                    p = Precinct.objects.create(
                            name = obj['name'],
                            coord_lat = obj['coord_lat'],
                            coord_lng = obj['coord_lng'],
                            coord_alt = obj['coord_alt'],
                            area = obj['area'],
                            count_yes = 0,
                            count_no = 0,
                            count_undecided = 0,
                            count_yardsign = 0
                            )
                    p.save()

        # If didn't pass in a list of precincts, use the default 
        # list from the database, this happens when user first 
        # loads the home page (without uploading own precinct file)
        else:
            precinct_objs = Precinct.objects.all()

    return render_to_response('vm/home_precinct_list.html', {'precinct_objs': precinct_objs}, context)

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
        else:
            print form.errors
    elif request.method == "GET":
        if voter_id:
            voter = Wasco.objects.get(pk = voter_id)
            form = VoteResponseForm(instance = voter)

    return render_to_response("vm/voter_response.html", {'form': form, 'voter': voter}, context)
