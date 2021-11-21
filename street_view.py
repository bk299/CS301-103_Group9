from os import path
import os
import google_streetview.api
import random

API_KEY = ''

# SECTION 0
min_lat = 37.5
max_lat = 45
min_long = -77.5
max_long = -67.5

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION0')


# SECTION 1
min_lat = 40
max_lat = 47.5
min_long = -92.5
max_long = -77.5

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION1')


# SECTION 2
min_lat = 25
max_lat = 37.5
min_long = -85
max_long = -75

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION2')


# SECTION 3
min_lat = 30
max_lat = 40
min_long = -100
max_long = -85

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION3')


# SECTION 4
min_lat = 40
max_lat = 49
min_long = -102.5
max_long = -92.5

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION4')


# SECTION 5
min_lat = 37.5
max_lat = 49
min_long = -115
max_long = -102.5

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION5')


# SECTION 6
min_lat = 31
max_lat = 37.5
min_long = -115
max_long = -100

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION6')


# SECTION 7
min_lat = 33
max_lat = 49
min_long = -125
max_long = -115

params = []
for i in range(222):
    lat_range = random.uniform(min_lat, max_lat)
    long_range = random.uniform(min_long, max_long)

    formatted_location = f'{lat_range},{long_range}'

    default_dict = {
        'size': '640x640',
        'location': formatted_location,
        'pitch': '0',
        'radius': '15000',
        'source': 'outdoor',
        'key': API_KEY
    }

    params.append(default_dict)

results = google_streetview.api.results(params)
results.download_links('SECTION7')


for i in range(8):
    folder_num = str(i)
    folder_name = f'SECTION{folder_num}'
    for j in range(250):
        file_num = str(j)
        file_name = f'{folder_name}/gsv_{file_num}.jpg'
        if path.exists(file_name):
            os.rename(file_name, f'{folder_name}/{file_num}.jpg')
