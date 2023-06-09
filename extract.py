"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_objects = []
    params_list = []
    with open(neo_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line in reader:
            params_list.append(line)
    for param in params_list:
        neo_objects.append(NearEarthObject(**param))
    return neo_objects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approach_objects = []
    params = []
    with open(cad_json_path, 'r', encoding='utf-8') as f:
        reader = json.load(f)
        keys = reader['fields']
        for values in reader['data']:
            params.append(dict(zip(keys, values)))
        for param in params:
            close_approach_objects.append(CloseApproach(**param))
        return close_approach_objects
