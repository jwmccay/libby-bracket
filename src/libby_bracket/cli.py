"""
Command line interface functions
"""


def get_matchup_input() -> int:

    valid_input = False

    while not valid_input:

        idx = input('> ')

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
