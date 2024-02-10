import json
import argparse

from libby_bracket.parse_libby import (
    get_json_from_file,
    cleanup_downloaded_timeline)

clean_ascii = r"""
    ___     ______ ______  ___     ______  __ _______ ___
   /  /    / ==  //  ___/ /  /    /  ___/ /  \\   _  \\  \
  /  /    /____< /  /    /  /    /  /__  /    \\  \\  \\  \
 /  /___ /     //  /___ /  /___ /  /___ /  __  \\  \\  \\  |
/______//_____//______//______//______//__/  \__\\__\\_____|
"""


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

    timeline_new, stats = cleanup_downloaded_timeline(
        timeline)

    output_name = f'libby_{args.job_id}_0.json'

    print("lbclean")
    print(clean_ascii)

    print(f"Out of {stats["original_count"]} events:")
    print(f"   {stats["duplicate_count"]} duplicates")
    print(f"   {stats["nonborrowed_count"]} non-borrow events")
    print(f"   {stats["nonborrowed_count"]} exported for review")


    output_json = {"version": 1,
                   "timeline": timeline_new}

    with open(output_name, 'w') as f:
        json.dump(output_json, f)
