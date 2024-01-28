"""
Sandbox
"""

import argparse
from random import shuffle
import json

from libby_bracket.parse_libby import get_json_from_file
from libby_bracket.matchup import matchup


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                        prog='getlibbydata',
                        description='Gets data from Libby')

    parser.add_argument('libby_json')  # positional argument
    parser.add_argument('-i', '--iteration')
    parser.add_argument('-n', '--comparisons')
    parser.add_argument('-a', '--compare_all', action='store_true')

    args = parser.parse_args()

    libby_json = get_json_from_file(args.libby_json)

    timeline = libby_json["timeline"]

    # TODO handle bad number of comparisons
    if not args.compare_all and args.comparisons is not None:
        timeline_winners = matchup(timeline,
            n_compare=int(args.comparisons))
    else:
        timeline_winners = matchup(timeline)

    output_json = {"version": 1,
                    "timeline": timeline_winners}

    with open(f'libby{args.iteration}.json', 'w') as f:
        json.dump(output_json, f)