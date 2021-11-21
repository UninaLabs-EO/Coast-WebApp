# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from glob import glob
import pandas as pd


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index', 
    )

@blueprint.route('/<template>')
@login_required
def route_template(template):

    df = pd.read_csv('apps\\templates\\home\\Adriatico\\CSK-SAO\\ALL_Adriatic_CSK-SAO.csv')

    CSK_adr_1 = df['CSK'].to_list() 
    SAO_adr_1 = df['SAO'].to_list()
    idx = df['Unnamed: 0'].to_list()


    hrefs = glob('apps\\templates\\home\\Adriatico\\CSK-SAO\\*.html')
    hrefs = sorted(hrefs, key=lambda x: int(x.split('_')[1].split('__')[0]))
    hrefs_adr_1 = [x.split('\\')[-1] for x in hrefs]

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, hrefs=hrefs_adr_1, CSK=CSK_adr_1, SAO=SAO_adr_1, idx=idx,
        )

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/CSK-SAO/<map>')
@login_required
def route_CSK_SAO(map):

    try:

        if not map.endswith('.html'):
            map += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/Adriatico/CSK-SAO/" + map, segment=segment)

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
