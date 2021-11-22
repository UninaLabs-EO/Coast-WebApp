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

from Router_Values import GetRouteValues

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index', 
    )


@blueprint.route('/<template>')
@login_required
def route_template(template):


    adr_csk_sao = GetRouteValues('apps\\templates\\home\\Adriatico\\CSK-SAO\\ALL_Adriatic_CSK-SAO.csv', 'apps\\templates\\home\\Adriatico\\CSK-SAO', 'CSK','SAO')
    adr_csk_sen = GetRouteValues('apps\\templates\\home\\Adriatico\\CSK-SEN\\ALL_Adriatic_CSK-SEN.csv','apps\\templates\\home\\Adriatico\\CSK-SEN', 'CSK','SEN' )

    alb_csk_sao = GetRouteValues('apps\\templates\\home\\Alborean\\CSK-SAO\\ALL_Alborean_CSK-SAO.csv', 'apps\\templates\\home\\Alborean\\CSK-SAO', 'CSK','SAO')
    alb_csk_sen = GetRouteValues('apps\\templates\\home\\Alborean\\CSK-SEN\\ALL_Alborean_CSK-SEN.csv', 'apps\\templates\\home\\Alborean\\CSK-SEN', 'CSK','SEN')

    ega_csk_sen = GetRouteValues('apps\\templates\\home\\Egadi\\CSK-SEN\\ALL_Egadi_CSK-SEN.csv', 'apps\\templates\\home\\Egadi\\CSK-SEN', 'CSK','SEN')




    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment,  
            a1=adr_csk_sao, a2=adr_csk_sen,
            b1=alb_csk_sao, b2=alb_csk_sen,
            c1=ega_csk_sen,
        )

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# @blueprint.route('Sardegna/CSK-SAO/<map>')
# @login_required
# def route_CSK_SAO4(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Sardegna/CSK-SAO/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500

# @blueprint.route('Sardegna/CSK-SEN/<map>')
# @login_required
# def route_CSK_SEN4(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Sardegna/CSK-SEN/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# @blueprint.route('Egadi/CSK-SEN/<map>')
# @login_required
# def route_CSK_SEN3(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Egadi/CSK-SEN/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# @blueprint.route('Alborean/CSK-SEN/<map>')
# @login_required
# def route_CSK_SEN2(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Alborean/CSK-SEN/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# @blueprint.route('Alborean/CSK-SAO/<map>')
# @login_required
# def route_CSK_SAO2(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Alborean/CSK-SAO/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500



# @blueprint.route('/CSK-SAO/<map>')
# @login_required
# def route_CSK_SAO(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Adriatico/CSK-SAO/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500

# @blueprint.route('/CSK-SEN/<map>')
# @login_required
# def route_CSK_SEN(map):

#     try:

#         if not map.endswith('.html'):
#             map += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/Adriatico/CSK-SEN/" + map, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
