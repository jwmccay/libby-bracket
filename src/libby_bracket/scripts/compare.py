"""
Main comparison script
"""

import argparse
import json

from libby_bracket.parse_libby import get_json_from_file
from libby_bracket.matchup import matchup

comp_ascii = r"""
    ___     ______ ______  _______ __    __ _______
   /  /    / ==  //  ___/ /  __  //  \  /  \\   _  \
  /  /    /____< /  /    /  / / //    \/    \\   -__\
 /  /___ /     //  /___ /  /_/ //  /\    /\  \\  \
/______//_____//______//______//__/  \__/  \__\\__\
"""
comp_instructions = r"""
For each comparison, type one of the prompted numbers and hit return.
"""


def compare():

    parser = argparse.ArgumentParser(
                        prog='getlibbydata',
                        description='Gets data from Libby')

    parser.add_argument('-j', '--job_id')
    parser.add_argument('-i', '--iteration')
    parser.add_argument('-n', '--comparisons')
    parser.add_argument('-a', '--compare_all', action='store_true')

    args = parser.parse_args()

    libby_json = get_json_from_file(
        f"libby_{args.job_id}_{args.iteration}.json"
    )

    timeline = libby_json["timeline"]

    print(comp_ascii[1:])
    print(comp_instructions)

    # TODO handle bad number of comparisons
    if not args.compare_all and args.comparisons is not None:
        results = matchup(timeline,
                          n_compare=int(args.comparisons))
    else:
        results = matchup(timeline)

    output_json = {"version": 1,
                   "timeline": results["timeline_winners"]}

    new_iteration = str(int(args.iteration) + 1)

    with open(f'libby_{args.job_id}_{new_iteration}.json', 'w') as f:
        json.dump(output_json, f)

    with open(f'winners_{args.job_id}_{new_iteration}.txt', 'w') as f:
        f.writelines(line + '\n' for line in results["winners"])
