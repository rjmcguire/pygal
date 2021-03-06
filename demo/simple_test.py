#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
import time
import sys
from math import cos, sin
from subprocess import call
from pygal import *
from pygal.style import *

lnk = lambda v, l=None: {'value': v, 'xlink': 'javascript:alert("Test %s")' % v, 'label': l}

t_start  = time.time()

gauge = Gauge()

gauge.range = [-10, 10]
gauge.add('Need l', [2.3, 5.12])
# gauge.add('No', [99, -99])
gauge.render_to_file('out-gauge.svg')

pyramid = Pyramid()

pyramid.x_labels = ['0-25', '25-45', '45-65', '65+']
pyramid.add('Man single', [2, 4, 2, 1])
pyramid.add('Woman single', [10, 6, 1, 1])
pyramid.add('Man maried', [10, 3, 4, 2])
pyramid.add('Woman maried', [3, 3, 5, 3])

pyramid.render_to_file('out-pyramid.svg')


funnel = Funnel()

funnel.add('1', [1, 2, 3])
funnel.add('3', [3, 4, 5])
funnel.add('6', [6, 5, 4])
funnel.add('12', [12, 2, 9])

funnel.render_to_file('out-funnel.svg')

dot = Dot()
dot.x_labels = map(str, range(4))

dot.add('a', [1, lnk(3, 'Foo'), 5, 3])
dot.add('b', [2, 2, 0, 2])
dot.add('c', [5, 1, 5, lnk(3, 'Bar')])
dot.add('d', [5, 5, lnk(0, 'Babar'), 3])

dot.render_to_file('out-dot.svg')


bar = Bar(style=styles['neon'])
bar.add('1234', [
    {'value': 10, 'label': 'Ten',    'xlink': 'http://google.com?q=10'},
    {'value': 20, 'label': 'Twenty', 'xlink': 'http://google.com?q=20'},
    30,
    {'value': 40, 'label': 'Forty',  'xlink': 'http://google.com?q=40'}
])

bar.add('4321', [40, {'value': 30, 'label': 'Thirty', 'xlink': 'http://google.com?q=30'}, 20, 10])
bar.x_labels = map(str, range(1, 5))
bar.logarithmic = True
bar.zero = 1
# bar.included_js = []
# bar.external_js = [
    # 'http://localhost:7575/svg.jquery.js',
    # 'http://localhost:7575/pygal.js',
# ]
bar.fill = True
bar.render_to_file('out-bar.svg')


hbar = HorizontalBar()
rng = [18, 9, 7, 3, 1, None, -5]
hbar.add('test1', rng)
rng2 = [16, 14, 10, 9, 7, 3, -1]
hbar.add('test2', rng2)
rng3 = [123, None, None, 4, None, 6]
hbar.add('test3', rng3)
hbar.x_labels = map(
    lambda x: '%s / %s' % x, zip(map(str, rng), map(str, rng2)))
hbar.title = "Horizontal Bar test"
hbar.render_to_file('out-horizontalbar.svg')

rng = [30, -32, 39, None, 12, lnk(21, '?')]
rng2 = [24, -8, lnk(18, '!'), 12]
rng3 = [6, 1, -10, 0]
config = Config()
config.x_label_rotation = 35
# config.x_labels = map(lambda x: '%s  / %s / %s' % x,
#                         zip(map(str, rng),
#                             map(str, rng2),
#                             map(str, rng3)))
config.title = "Stacked Bar test"
config.style = NeonStyle

stackedbar = StackedBar(config)
stackedbar.add('@@@@@@@', rng)
stackedbar.add('++++++', rng2)
stackedbar.add('--->', rng3)
stackedbar.add('None', [None, 42, 42])
stackedbar.render_to_file('out-stackedbar.svg')

config.title = "Horizontal Stacked Bar test"
hstackedbar = HorizontalStackedBar(config)
hstackedbar.add('@@@@@@@', rng)
hstackedbar.add('++++++', rng2)
hstackedbar.add('--->', rng3)

hstackedbar.render_to_file('out-horizontalstackedbar.svg')

line = Line(Config(style=NeonStyle,
                   zero=.0001, fill=True,
                   human_readable=not True, logarithmic=not True))
rng = range(-30, 31, 1)

# line.add('test1', [1000 ** cos(x / 10.) for x in rng])
# line.add('test2', [1000 ** sin(x / 10.) for x in rng])
# line.add('test3', [1000 ** (cos(x / 10.) - sin(x / 10.)) for x in rng])
# rng = range(1, 2000, 25)
# line.add('x', rng)
# line.add('x', rng)
# line.add('10^10^x', map(lambda x: ((x / 333.) ** (x / 333.)), rng))
# line.add('None', [None, None, None, 12, 31, 11, None, None, 12, 14])
# line.add('2', [None, None, 2, 4, 8, None, 14, 10, None])
# line.add('1', [1, 5, 3, 4, 6, 12, 13, 7, 2])
# line.add('1', [.000000091, .000000094, .000092])
# line.add('_', [2 ** -3, 2.9 ** -8, 2])
# line.add('_', [.001, .0001, .00001])
# line.add('_', [1 + 10 ** 10, 3 + 10 ** 10, 2 + 10 ** 10])
# line.add('_', [1, lnk(4), None,  2, 8, lnk(-2), None, lnk(2)])
line.add('_', [0, .5, 1])
line.x_labels = map(str, rng)
line.order_min = 0
line.title = "Line test"
# line.range = (40000, 70000)
# line.y_labels = [40000, 50000, 60000, 70000]
# line.interpolate = "cubic"
line.interpolation_precision = 200
line.render_to_file('out-line.svg')

stackedline = StackedLine(fill=True)
stackedline.add('test1u euirset uriets ur itseruie uriset uriest u', [1, 3, 2, None, 2, 13, 2, 5, 8])
stackedline.add('test2', [4, 1, 1,  3, 12,  3])
stackedline.add('test3', [9, 3, 2, lnk(10, '!'),  8,  2])
stackedline.x_labels = ['aaisaruistarsitauritaria', 'bsruie trstie rusiet ruetsru', 'cuasitaruisrnauciuestuirue uiretsu iersut irasui', 'd', 'e', 'f', 'g'] 
stackedline.title = "Stackedline ine uisernuis enuir esnue sunres nuise nuires uinsre auin ruist arusit arst ierustie ruiset uriest uirest test"
# stackedline.interpolate = "cubic"xb

stackedline.render_to_file('out-stackedline.svg')

xy = XY(Config(fill=True, style=NeonStyle, interpolate='cubic'))
xy.add('test1', [(1981, 1), (1999, -4), (2001, 2), (2003, 10), (2012, 8)])
xy.add('test2', [(1988, -1), (1986, 12), (2007, 7), (2010, 4)])
xy.add('test2', [(None, None), (None, 12), (2007, None), (2002.3, 12)])
# xy.add('test2', [(1980, 0), (1985, 2), (1995, -2), (2005, 4), (2020, -4)])
                 # (2005, 6), (2010, -6), (2015, 3), (2020, -3), (2025, 0)])
xy.title = "XY test"
xy.render_to_file('out-xy.svg')

pie = Pie(Config(style=NeonStyle))
# pie.add('test', [lnk(11, 'Foo'), {'value': 8, 'label': 'Few'}, 21])
# pie.add('test2', [lnk(29), None, 9])
# pie.add('test3', [24, 10, 32])
# pie.add('test4', [20, lnk(18), 9])
# pie.add('test5', [17, 5, 10])
# pie.add('test6', [None, None, 10])
for i in range(10):
    pie.add('P' + str(i) + '!' * i, [i, 30 - i])

pie.js = [
    'http://localhost:9898/svg.jquery.js',
    'http://localhost:9898/pygal-tooltips.js',
]
# pie.add('test', {'value': 11, 'xlink': 'javascript:alert("lol 11")'})
# pie.add('test2', 1)
# pie.add('test3', 5)
# pie.title = "Pie test"
pie.legend_at_bottom = True
pie.legend_box_size = 10
pie.render_to_file('out-pie.svg')

config = Config()
config.fill = True
config.style = NeonStyle
config.x_labels = (
    'black', 'red', 'blue', 'yellow', 'orange', 'green', 'white')
# config.interpolate = 'nearest'
radar = Radar(config)
radar.add('test', [1, 4, lnk(10), 5, None, 2, 5])
radar.add('test2', [10, 2, 0, 5, 1, 9, 4])

radar.title = "Radar test"

radar.render_to_file('out-radar.svg')

# call(['wsreload', '--url', "file:///*/*/kozea/pygal/*"])

print "Ok (%dms)" % (1000 * (time.time() - t_start))

if '-t' in sys.argv:
    import pytest
    pytest.main('')
