#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import pandas as pd

# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.models import HoverTool

# Get File Directory
WORK_DIR = os.path.dirname((os.path.realpath(__file__)))

# Read the csv files
player_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv(
    WORK_DIR + '/data/2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv(
    WORK_DIR + '/data/2017-18_standings.csv', parse_dates=['stDate'])

# Find players who took at least 1 three-point shot during the season
three_takers = player_stats[player_stats['play3PA'] > 0]

# Clean up the player names, placing them in a single column
three_takers['name'] = [
    f'{p["playFNm"]} {p["playLNm"]}' for _, p in three_takers.iterrows()
]

# Aggregate the total three-point attempts and makes for each player
three_takers = (three_takers.groupby(
    'name').sum().loc[:, ['play3PA', 'play3PM']].sort_values(
        'play3PA', ascending=False))

# Filter out anyone who didn't take at least 100 three-point shots
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()

# Add a column with a calculated three-point percentage (made/attempted)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']

# Output to file
output_file(
    'three-point-att-vs-pct.html', title='Three-Point Attempts vs. Percentage')

# Store the data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Specify the selection tools to be made available
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Create the figure
fig = figure(
    plot_height=400,
    plot_width=600,
    x_axis_label='Three-Point Shots Attempted',
    y_axis_label='Percentage Made',
    title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
    toolbar_location='below',
    tools=select_tools)

# Format the y-axis tick labels as percentages
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# Add square representing each player
fig.square(
    x='play3PA',
    y='pct3PM',
    source=three_takers_cds,
    color='royalblue',
    selection_color='deepskyblue',
    nonselection_color='lightgray',
    nonselection_alpha=0.3)

# Format the tooltip
tooltips = [
    ('Player', '@name'),
    ('Three-Pointers Made', '@play3PM'),
    ('Three-Pointers Attempted', '@play3PA'),
    ('Three-Point Percentage', '@pct3PM{00.0%}'),
]

# Configure a renderer to be used upon hover
hover_glyph = fig.circle(
    x='play3PA',
    y='pct3PM',
    source=three_takers_cds,
    size=15,
    alpha=0,
    hover_fill_color='black',
    hover_alpha=0.5)

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

# Visualize
show(fig)
