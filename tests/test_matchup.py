"""
Test the matchup function.
"""

import random

import pytest

from libby_bracket.parse_libby import get_json_from_file
from libby_bracket.matchup import matchup


@pytest.fixture
def timeline_even():

    artifact_path = "tests/artifacts/borrowed_only_even.json"
    libby_json = get_json_from_file(artifact_path)

    return libby_json["timeline"]


@pytest.fixture
def timeline_odd():

    artifact_path = "tests/artifacts/borrowed_only_odd.json"
    libby_json = get_json_from_file(artifact_path)

    return libby_json["timeline"]


def test_matchup_even(timeline_even, monkeypatch):
    """Test the winners of a json with an even number of entries.
    """

    random.seed(a=1, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_even)

    assert results["winners"][0] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert results["winners"][1] == "A Matter of Profit by Hilari Bell"
    assert results["losers"][0] == "Lirael by Garth Nix"
    assert results["losers"][1] == "Out of the Silent Planet by C. S. Lewis"


def test_matchup_even_timeline(timeline_even, monkeypatch):
    """Test the timeline of a json with an even number of entries.
    """

    random.seed(a=1, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_even)
    timeline = results["timeline_winners"]

    assert timeline[0]["title"]["text"] == "Interpreter of Maladies"
    assert timeline[1]["title"]["text"] == "A Matter of Profit"
    assert timeline[0]["author"] == "Jhumpa Lahiri"
    assert timeline[1]["author"] == "Hilari Bell"


def test_matchup_odd(timeline_odd, monkeypatch):
    """Test the winners of a json with an odd number of entries. The
    odd one out should also be included.
    """

    random.seed(a=2, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_odd)

    assert results["winners"][0] == "Out of the Silent Planet by C. S. Lewis"
    assert results["winners"][1] == "Lirael by Garth Nix"
    assert results["winners"][2] == \
        "The Left Hand of Darkness by Ursula K. Le Guin"
    assert results["losers"][0] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert results["losers"][1] == "A Matter of Profit by Hilari Bell"


def test_matchup_odd_timeline(timeline_odd, monkeypatch):
    """Test the timeline of a json with an odd number of entries. The
    odd one out should also be included.
    """

    random.seed(a=2, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_odd)
    timeline = results["timeline_winners"]

    assert timeline[0]["title"]["text"] == "Out of the Silent Planet"
    assert timeline[0]["author"] == "C. S. Lewis"
    assert timeline[1]["title"]["text"] == "Lirael"
    assert timeline[1]["author"] == "Garth Nix"
    assert timeline[2]["title"]["text"] == "The Left Hand of Darkness"
    assert timeline[2]["author"] == "Ursula K. Le Guin"


def test_matchup_subset(timeline_odd, monkeypatch):
    """Test a subset of the odd json.
    """

    random.seed(a=2, version=2)

    cli_inputs = iter(["2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_odd, n_compare=1)
    timeline = results["timeline_winners"]

    assert results["winners"][0] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert len(results["winners"]) == 1
    assert timeline[0]["title"]["text"] == "Interpreter of Maladies"
    assert timeline[0]["author"] == "Jhumpa Lahiri"


def test_matchup_subset_both_win(timeline_odd, monkeypatch):
    """Test a subset using the "both win" option
    """

    random.seed(a=2, version=2)

    # both win
    cli_inputs = iter(["3"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_odd, n_compare=1)
    timeline = results["timeline_winners"]

    assert results["winners"][0] == "Lirael by Garth Nix"
    assert timeline[0]["title"]["text"] == "Lirael"
    assert timeline[0]["author"] == "Garth Nix"

    assert results["winners"][1] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert timeline[1]["title"]["text"] == "Interpreter of Maladies"
    assert timeline[1]["author"] == "Jhumpa Lahiri"

    assert len(results["winners"]) == 2


def test_matchup_both_lose(timeline_odd, monkeypatch):
    """Test using the "both lose" option
    """

    random.seed(a=4, version=2)

    # 1 wins first, both lose second
    cli_inputs = iter(["1", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_odd)
    timeline = results["timeline_winners"]

    assert results["winners"][0] == "A Matter of Profit by Hilari Bell"
    assert timeline[0]["title"]["text"] == "A Matter of Profit"
    assert timeline[0]["author"] == "Hilari Bell"

    assert results["winners"][1] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert timeline[1]["title"]["text"] == "Interpreter of Maladies"
    assert timeline[1]["author"] == "Jhumpa Lahiri"

    assert len(results["winners"]) == 2
