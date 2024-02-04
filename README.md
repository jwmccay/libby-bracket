# Libby Bracket

A very simple command line tool to review and rank reading history from Libby. It's a minimum viable product. The only goal is reminding the author about their favorite books.

## Installation

```shell
git clone https://github.com/jwmccay/libby-bracket.git
cd libby-bracket
pip install .
```

## Usage

You'll need the URL of your Libby timeline. This can can be found in the app in `Timeline/Actions/Export Timeline`.

Note that the tool is an MVP, and there is minimal checking of inputs. It will have undefined behavior if you give it a bad command line flag or choose a number of comparisons that is too large or small.

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

## Development

To develop, install as an editable package with optional development dependencies.

```shell
pip install -e .[dev]
```