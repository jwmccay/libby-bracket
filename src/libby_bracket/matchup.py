"""
Functions to run a set of matches.
"""

from random import shuffle

from libby_bracket.cli import get_matchup_input


def matchup(timeline, n_compare=None):

    shuffle(timeline)

    winners = []
    losers = []
    timeline_winners = []

    timeline_length = len(timeline)
    half_length_int = int(timeline_length / 2)

    timeline_1 = timeline[:half_length_int]
    timeline_2 = timeline[half_length_int:]

    # handle case where user wants to compare all entries
    if n_compare is None:

        n_compare = half_length_int

        # if odd number of entries, always keep last
        if (timeline_length % 2) != 0:
            timeline_winners.append(timeline[-1])
            description_odd = timeline[-1]["title"]["text"] \
                + " by " + timeline[-1]["author"]
            winners.append(description_odd)

    for i in range(n_compare):
        print(i + 1, "out of", n_compare)

        description_1 = timeline_1[i]["title"]["text"] \
            + " by " + timeline_1[i]["author"]

        description_2 = timeline_2[i]["title"]["text"] \
            + " by " + timeline_2[i]["author"]

        print("   1 ", description_1)
        print("   2 ", description_2)
        print("   3  Both win :)")
        print("   4  Both lose :(")

        # TODO make this adapt to number of inputs
        idx = get_matchup_input()

        if idx == 1:
            winners.append(description_1)
            losers.append(description_2)
            timeline_winners.append(timeline_1[i])
        elif idx == 2:
            winners.append(description_2)
            losers.append(description_1)
            timeline_winners.append(timeline_2[i])
        elif idx == 3:
            winners.append(description_1)
            winners.append(description_2)
            timeline_winners.append(timeline_1[i])
            timeline_winners.append(timeline_2[i])
        elif idx == 4:
            losers.append(description_1)
            losers.append(description_2)
        else:
            print("Bad input!")

    results = {
        "timeline_winners": timeline_winners,
        "winners": winners,
        "losers": losers}

    return results
