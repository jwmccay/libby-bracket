"""
Get data to use
"""

import json

import requests


def get_json_from_url(libby_url: str) -> dict:

    r = requests.get(libby_url)
    libby_json = json.loads(r.text)

    return libby_json


def get_json_from_file(libby_json_path: str) -> dict:

    with open(libby_json_path, 'r') as f:
        libby_json = json.load(f)

    return libby_json
