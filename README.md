# Libby Bracket

A very simple command line tool to review and rank reading history from Libby. It's a minimum viable product. The only goal is reminding the author about their favorite books.

## Installation

```shell
git clone https://github.com/jwmccay/libby-bracket.git
cd libby-bracket
pip install .
```

## Usage

The package creates three command line programs.
- `lbfetch` gets a json of your Libby timeline from a URL (can be found in the app in `Timeline/Actions/Export Timeline`)
- `lbclean` removes duplicates
- `lbcomp` starts an interactive session where you input which of two books you like better. It is intended to be run several times, with each run being a level of the bracket.

Note that the tool is an MVP, and there is minimal checking of inputs. It will have undefined behavior if you give it a bad command line flag or choose a number of comparisons that is too large or small.

### Example

```shell
# Get data from libby. The job ID (-j) tags all output files. Creates
# `libby_download_mytag.json`
lbfetch -j mytag https://share.libbyapp.com/data/<some-numbers>/libbytimeline-activities.json

# Remove duplicates and only consider `Borrow` activities. Reads the
# downloaded json and creates the `libby_mytag_0.json`
lbclean -j mytag

# Do 25 random comparisons from the `0` json. The iteration flag (-i)
# refers to the comparison iteration. Writes winners to
# `libby_mytag_1.json` and `winners_mytag_1.txt`
lbcomp -j mytag -n 25 -i 0

# Compare all entries in the `1` json. Reads the `1` json and writes
# the `2` json
lbcomp -j mytag -a -i 1
```

## Development

To develop, install as an editable package with optional development dependencies.

```shell
pip install -e .[dev]
```