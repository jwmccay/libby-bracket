"""
Clean up libby data.
"""

import json
import argparse

from book_rank.parse_libby import get_json_from_file


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog='cleanlibbydata',
                        description='CLean data from Libby')

    parser.add_argument('libby_json')  # positional argument

    args = parser.parse_args()

    libby_json = get_json_from_file(args.libby_json)

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

    with open(f'libby.json', 'w') as f:
        json.dump(output_json, f)
