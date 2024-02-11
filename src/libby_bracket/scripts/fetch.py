"""
Download data from Libby.
"""

import argparse
import json

from libby_bracket.parse_libby import get_json_from_url


fetch_ascii = r"""
    ___     ______ ______ ______ ______ ______  ___   ___
   /  /    / ==  //  ___//  ___//_   _//  ___/ /  /__/  /
  /  /    /____< /  /__ /  /__   /  / /  /    /        /
 /  /___ /     //  ___//  /___  /  / /  /___ /  ___   /
/______//_____//__/   /______/ /__/ /______//__/  /__/
"""


def fetch():

    parser = argparse.ArgumentParser(
                        prog='getlibbydata',
                        description='Gets data from Libby')

    parser.add_argument('libby_url')  # positional argument
    parser.add_argument('-j', '--job_id')

    print(fetch_ascii)

    args = parser.parse_args()

    libby_json = get_json_from_url(args.libby_url)

    output_name = f'libby_download_{args.job_id}.json'

    with open(output_name, 'w') as f:
        json.dump(libby_json, f)

    print("Saved to", output_name)
