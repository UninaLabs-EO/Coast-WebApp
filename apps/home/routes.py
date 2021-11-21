# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from LeanspaceAPI import GetMetric

@blueprint.route('/index')
@login_required
def index():

    altitude_id = 'ced4142b-d918-4821-839a-6428130b97ef'
    alt = GetMetric(altitude_id)
    alt = alt['data'][0]['telemetry_debris.d_'+altitude_id.replace('-','_')]

    latitude_id = 'ac3c553d-f6b2-4a89-8d5c-8cb05db9d96e'
    lat = GetMetric(latitude_id)
    lat = lat['data'][0]['telemetry_debris.d_'+latitude_id.replace('-','_')]

    longitude_id = 'ac3c553d-f6b2-4a89-8d5c-8cb05db9d96e'
    lon = GetMetric(longitude_id)
    lon = lon['data'][0]['telemetry_debris.d_'+longitude_id.replace('-','_')]

    battery_dod_id = '03d4336b-3c51-4103-9444-889cc24d5298'
    dod = GetMetric(battery_dod_id)
    dod = dod['data'][0]['telemetry_debris.d_'+battery_dod_id.replace('-','_')]

    # bus_voltage_id = '673f78c2-afd1-4670-bd17-392847a0dbe4'
    # volt = GetMetric(bus_voltage_id)
    # if len(volt)>1:
    #     volt = volt[0]['telemetry_debris.d_'+bus_voltage_id.replace('-','_')]
    # else:
    #     volt['telemetry_debris.d_'+bus_voltage_id.replace('-','_')]

    # vespa_dist_id = 'be3ca13a-b38e-4e95-a6ab-0607ca7be1ab'
    # vdist = GetMetric(vespa_dist_id)
    # vdist = vdist['data'][0]['telemetry_debris.d_'+vespa_dist_id.replace('-','_')]

    # vespa_state_id='8939914e-8b1b-45ac-8734-95081e486de4'
    # vstate = GetMetric(vespa_state_id)

    return render_template('home/index.html', segment='index', alt=alt, lat=lat, lon=lon,
    dod = dod,
    )

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
