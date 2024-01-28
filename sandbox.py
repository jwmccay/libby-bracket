"""
Sandbox
"""

from random import randrange

from book_rank.parse_libby import get_json_from_file


def get_cli_input() -> int:

    valid_input = False
    while not valid_input:
        s = input('--> ')
        idx = int(s)
        if idx == 1:
            valid_input = True
        elif idx == 2:
            valid_input = True
        elif idx == 3:
            valid_input = True
        else:
            valid_input = False
    return idx


if __name__ == "__main__":

    libby_json = get_json_from_file("libby.json")

    timeline = libby_json["timeline"]

    timeline_length = len(timeline)

    winners = []
    losers = []

    n_compare = 2

    for i in range(n_compare):
        print(i)

        n1 = randrange(0, timeline_length)
        n2 = randrange(0, timeline_length)

        print("   1 ",
              timeline[n1]["title"]["text"],
              "by", timeline[n1]["author"])
        print("   2 ",
              timeline[n2]["title"]["text"],
              "by", timeline[n2]["author"])
        print("   3  Did not read either :/")

        idx = get_cli_input()

        if idx == 1:
            winners.append(n1)
            losers.append(n2)
        elif idx == 2:
            winners.append(n2)
            losers.append(n1)
        elif idx == 3:
            losers.append(n1)
            losers.append(n2)
