#gives access to the system
# from arcgis.gis import GIS

import arcgis
from arcgis.geocoding import reverse_geocode

import csv, json
from app import models

def geocoding(latitude, longitude):
    """
    Geocodes the address basing on latitude and longitude
    """
    gis = arcgis.gis.GIS("https://www.arcgis.com/", "Niktia", "polo8Ret")

    results = arcgis.geocoding.reverse_geocode([latitude, longitude])

    return results


# CSV to JSON converter
def convert(file_path):
    """"
    Function converts csv file to JSON
    """
    # Retrieve the pass of the CSV file
    csv_file_path = file_path
    json_file_path = 'static/files/result.json'

    # Storing data
    data = {}

    # converting CSV to JSON format
    with open(csv_file_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            point = csvRow['point']
            data[point] = csvRow

    converted_data = {}

    for key, value in data:
        name = key
        latitude = value['latitude']
        longitude = value['longitude']
        address = geocoding(latitude, longitude)

        converted_data[name] = address

    return converted_data








