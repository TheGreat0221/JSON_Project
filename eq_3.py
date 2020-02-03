import plotly
import json

in_file = open('eq_data_30_day_m1.json','r')
out_file = open('readable_eq_data.json','w')

eq_data = json.load(in_file)

print(type(eq_data))

json.dump(eq_data,out_file,indent=4)

list_of_eqs = eq_data['features']

print(type(list_of_eqs))
print(len(list_of_eqs)) ## how many earthquakes in our list (each dictionary is an earthquake)

mags        = []
lons        = []
lats        = []
hover_texts  = []

for eq in list_of_eqs:
    mag         = eq['properties']['mag']
    lon         = eq['geometry']['coordinates'][0]
    lat         = eq['geometry']['coordinates'][1]
    hover_text  = eq['properties']['title']
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

print(mags[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text':hover_texts,
        'marker':{
            'size':[5*mag for mag in mags], ## list comprehension (goes through each value in mags, and multiplies each val by 5)
            'color':mags,
            'colorscale':'Viridis',
            'reversescale':True,
            'colorbar':{'title':'Magnitude'}
        },

}]

my_layout = Layout(title="Global Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='Global_Earthquakes.html')