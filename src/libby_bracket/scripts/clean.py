import json
import argparse

from libby_bracket.parse_libby import get_json_from_file


def clean():

    parser = argparse.ArgumentParser(
                        prog='cleanlibbydata',
                        description='Clean data from Libby')

    # parser.add_argument('libby_json')  # positional argument
    parser.add_argument('-j', '--job_id')

    args = parser.parse_args()

    libby_json = get_json_from_file(
        f"libby_download_{args.job_id}.json")

    timeline = libby_json["timeline"]

    timeline_new = []
    titles = []

    for event in timeline:

        check_duplicates = any(
            [event["title"]["text"] == title for title in titles])

        if event["activity"] == "Borrowed" and not check_duplicates:
            timeline_new.append(event)
            titles.append(event["title"]["text"])

    output_json = {"version": 1,
                   "timeline": timeline_new}

    with open(f'libby_{args.job_id}_0.json', 'w') as f:
        json.dump(output_json, f)
