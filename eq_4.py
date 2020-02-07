import csv_functions as fn
import plotly
import json
import csv

## GRAB RAW DATA FROM FILE
in_file_2019 = open('MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt','r')

eq_csv = csv.reader(in_file_2019, delimiter=",")
lat_index,lon_index,bright_index,date_index = fn.get_headers(eq_csv)

## CREATE LIST TO AGGREGATE EVERYTHING INTO
list_lats    = []
list_lons    = []
list_brights = []
list_dates   = []

## AGGREGATE THE DATA FROM THE CSV FILE INTO RESPECTIVE LISTS 
list_lats,list_lons,list_brights,list_dates = fn.get_data(eq_csv,list_lats,list_lons,list_brights,list_dates,lat_index,lon_index,bright_index,date_index)

##print(list_lats)
## PLOT DATA 

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
        'type': 'scattergeo',
        'lon': list_lons,
        'lat': list_lats,
        'text':list_dates,
        'marker':{
            'size':[brightness/15 for brightness in list_brights], ## sized by level of brightness
            'color':list_brights,
            'colorscale':'Viridis',
            'reversescale':True,
            'colorbar':{'title':'Brightness'}
        },

}]

my_layout = Layout(title="Austrialian Fires - November 2019")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='Austrialian_Fires_2019.html')

print("Success?")
