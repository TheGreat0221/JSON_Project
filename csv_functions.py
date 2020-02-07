import csv 
from datetime import datetime

def get_headers(csv_file):

    header_row = next(csv_file)

    for index,column_header in enumerate(header_row):
        if column_header == "latitude":
            lat = index
        if column_header == "longitude":
            lon = index
        if column_header == "brightness":
            bright = index
        if column_header == "acq_date":
            date = index
    
    return(lat,lon,bright,date)

def get_data(csv_file,lats,lons,brights,dates,lat_index,lon_index,bright_index,date_index):

    for row in csv_file:
        try:
            lat = float(row[lat_index])
            lon = float(row[lon_index])
            bright = float(row[bright_index])
            current_date = row[date_index]
            
        except ValueError:
            print(f"Missing data for {current_date}")
            
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
            dates.append(current_date)

    return (lats,lons,brights,dates)