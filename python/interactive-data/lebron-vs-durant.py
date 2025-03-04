#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bokeh Visualization Template

This template is a general outline for turning your data into a
visualization using Bokeh.
"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Read the csv files
player_stats = pd.read_csv(WORK_DIR + '/data/2017-18_playerBoxScore.csv',
                           parse_dates=['gmDate'])
team_stats = pd.read_csv(WORK_DIR + '/data/2017-18_teamBoxScore.csv',
                         parse_dates=['gmDate'])
standings = pd.read_csv(WORK_DIR + '/data/2017-18_standings.csv',
                        parse_dates=['stDate'])

# Output inline in the notebook
output_file('lebron-vs-durant.html', title='LeBron James vs. Kevin Durant')

# Store the data in a ColumnDataSource
player_gm_stats = ColumnDataSource(player_stats)

# Create a view for each player
lebron_filters = [
    GroupFilter(column_name='playFNm', group='LeBron'),
    GroupFilter(column_name='playLNm', group='James')
]
lebron_view = CDSView(source=player_gm_stats, filters=lebron_filters)

durant_filters = [
    GroupFilter(column_name='playFNm', group='Kevin'),
    GroupFilter(column_name='playLNm', group='Durant')
]
durant_view = CDSView(source=player_gm_stats, filters=durant_filters)

# Consolidate the common keyword arguments in dicts
common_figure_kwargs = {
    'plot_width': 400,
    'x_axis_label': 'Points',
    'toolbar_location': None,
}
common_circle_kwargs = {
    'x': 'playPTS',
    'y': 'playTRB',
    'source': player_gm_stats,
    'size': 12,
    'alpha': 0.7,
}
common_lebron_kwargs = {
    'view': lebron_view,
    'color': '#002859',
    'legend': 'LeBron James'
}
common_durant_kwargs = {
    'view': durant_view,
    'color': '#FFC324',
    'legend': 'Kevin Durant'
}

# Create the two figures and draw the data
hide_fig = figure(**common_figure_kwargs,
                  title='Click Legend to HIDE Data',
                  y_axis_label='Rebounds')
hide_fig.circle(**common_circle_kwargs, **common_lebron_kwargs)
hide_fig.circle(**common_circle_kwargs, **common_durant_kwargs)

mute_fig = figure(**common_figure_kwargs, title='Click Legend to MUTE Data')
mute_fig.circle(**common_circle_kwargs,
                **common_lebron_kwargs,
                muted_alpha=0.1)
mute_fig.circle(**common_circle_kwargs,
                **common_durant_kwargs,
                muted_alpha=0.1)

# Add interactivity to the legend
hide_fig.legend.click_policy = 'hide'
mute_fig.legend.click_policy = 'mute'

# Visualize
show(row(hide_fig, mute_fig))
