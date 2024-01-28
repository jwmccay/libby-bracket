"""
Download data from Libby.
"""

import argparse
import json

from book_rank.parse_libby import get_json_from_url


if __name__ == "__main__":


    parser = argparse.ArgumentParser(
                        prog='getlibbydata',
                        description='Gets data from Libby')

    parser.add_argument('libby_url')  # positional argument

    args = parser.parse_args()

    libby_json = get_json_from_url(args.libby_url)

    # print(json.dumps(libby_json, indent=2))

    with open('libby_download.json', 'w') as f:
        json.dump(libby_json, f)
