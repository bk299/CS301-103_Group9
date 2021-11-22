import os
from os import path
import google_streetview.api
import random

API_KEY = ''


def get_streetview(min_lat, max_lat, min_long, max_long, number_images, section_name):
    params = []
    for i in range(number_images):
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
    results.download_links(f'{section_name}')


def rename_pictures():
    for i in range(8):
        folder_num = str(i)
        folder_name = f'SECTION{folder_num}'
        for j in range(250):
            file_num = str(j)
            file_name = f'{folder_name}/gsv_{file_num}.jpg'
            if path.exists(file_name):
                os.rename(file_name, f'{folder_name}/{file_num}.jpg')
    

# SECTION 0
min_lat = 37.5
max_lat = 45
min_long = -77.5
max_long = -67.5

get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION0')


# SECTION 1
min_lat = 40
max_lat = 47.5
min_long = -92.5
max_long = -77.5
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION1')


# SECTION 2
min_lat = 25
max_lat = 37.5
min_long = -85
max_long = -75
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION2')


# SECTION 3
min_lat = 30
max_lat = 40
min_long = -100
max_long = -85
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION3')


# SECTION 4
min_lat = 40
max_lat = 49
min_long = -102.5
max_long = -92.5
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION4')


# SECTION 5
min_lat = 37.5
max_lat = 49
min_long = -115
max_long = -102.5
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION5')


# SECTION 6
min_lat = 31
max_lat = 37.5
min_long = -115
max_long = -100
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION6')


# SECTION 7
min_lat = 33
max_lat = 49
min_long = -125
max_long = -115
get_streetview(min_lat, max_lat, min_long, max_long, 222, 'SECTION7')


rename_pictures()
