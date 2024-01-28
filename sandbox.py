"""
Sandbox
"""

from random import shuffle

from book_rank.parse_libby import get_json_from_file


def get_cli_input() -> int:

    valid_input = False
    
    while not valid_input:

        idx = input('--> ')
        
        if idx == "1":
            valid_input = True
            idx = 1
        elif idx == "2":
            valid_input = True
            idx = 2
        elif idx == "3":
            valid_input = True
            idx = 3
        elif idx == "4":
            valid_input = True
            idx = 4
        else:
            valid_input = False
            idx = None

    return idx


if __name__ == "__main__":

    libby_json = get_json_from_file("libby.json")

    timeline = libby_json["timeline"]

    shuffle(timeline)

    timeline_length = len(timeline)

    # TODO: handle odd timeline lengths
    timeline_1 = timeline[:int(timeline_length / 2)]
    timeline_2 = timeline[int(timeline_length / 2):]

    winners = []
    losers = []
    winners_full = []

    n_compare = 2

    for i in range(n_compare):
        print(i)

        description_1 = timeline_1[i]["title"]["text"] \
            + " by " + timeline_1[i]["author"]

        description_2 = timeline_2[i]["title"]["text"] \
            + " by " + timeline_2[i]["author"]

        print("   1 ", description_1)
        print("   2 ", description_2)
        print("   3  Both win :)")
        print("   4  Both lose :(")

        idx = get_cli_input()

        if idx == 1:
            winners.append(description_1)
            losers.append(description_2)
            winners_full.append(timeline_1[i])
        elif idx == 2:
            winners.append(description_2)
            losers.append(description_1)
            winners_full.append(timeline_2[i])
        elif idx == 3:
            winners.append(description_1)
            winners.append(description_2)
            winners_full.append(timeline_1[i])
            winners_full.append(timeline_2[i])
        elif idx == 4:
            losers.append(description_1)
            losers.append(description_2)
        else:
            print("Bad input!")
