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


def cleanup_downloaded_timeline(timeline):
    """Remove duplicates and non-Borrow events
    """

    timeline_new = []
    titles = []
    duplicate_count = 0
    nonborrowed_count = 0

    for event in timeline:

        check_duplicates = any(
            [event["title"]["text"] == title for title in titles])

        if check_duplicates and event["activity"] == "Borrowed":
            duplicate_count += 1

        if event["activity"] != "Borrowed":
            nonborrowed_count += 1

        if event["activity"] == "Borrowed" and not check_duplicates:
            timeline_new.append(event)
            titles.append(event["title"]["text"])

    duplicate_stats = {"original_count": len(timeline),
                       "duplicate_count": duplicate_count,
                       "nonborrowed_count": nonborrowed_count,
                       "new_count": len(timeline_new)}

    return timeline_new, duplicate_stats
