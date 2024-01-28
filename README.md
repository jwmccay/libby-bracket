# Libby Bracket

A very simple command line tool to review and rank reading history from Libby. It's a minimum viable product. The only goal is reminding the author about their favorite books.

## Installation

## Usage

```shell
# get data from libby
lbfetch -j jwm https://share.libbyapp.com/data/<some-numbers>/libbytimeline-activities.json

# remove duplicates and only consider `Borrow` activities
# creates the `0` json
lbclean -j jwm

# do 8 random comparisons from the `0` json
# creates the `1` json
lbcompare -j jwm -n 8 -i 0

# compare all entries in the `1` json
lbcompare -j jwm -a -i 1
```