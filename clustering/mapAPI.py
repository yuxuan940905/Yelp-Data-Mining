# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 03:53:52 2018

@author: Wenqi Zheng
"""
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap



def mapOut(gmap_api,long,la):
    output_file("gmap.html")
    map_options = GMapOptions(lat=42.35, lng=-71.1, map_type="roadmap", zoom=11)
    
    # For GMaps to function, Google requires you obtain and enable an API key:
    #
    #     https://developers.google.com/maps/documentation/javascript/get-api-key
    #
    # Replace the value below with your personal API key:
    p = gmap(gmap_api, map_options, title="All restarants serves pizza in Boston")
    
    source = ColumnDataSource(
        data=dict(lat=la,
                  lon=long)
        )
    
    p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)
    
    show(p)