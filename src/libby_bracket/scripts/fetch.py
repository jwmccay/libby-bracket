"""
Download data from Libby.
"""

import argparse
import json

from libby_bracket.parse_libby import get_json_from_url


def fetch():

    parser = argparse.ArgumentParser(
                        prog='getlibbydata',
                        description='Gets data from Libby')

    parser.add_argument('libby_url')  # positional argument
    parser.add_argument('-j', '--job_id')

    args = parser.parse_args()

    libby_json = get_json_from_url(args.libby_url)

    with open(f'libby_download_{args.job_id}.json', 'w') as f:
        json.dump(libby_json, f)