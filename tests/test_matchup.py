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


def test_matchup_even(timeline_even, monkeypatch):

    random.seed(a=1, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_even)

    assert results["winners"][0] == "Interpreter of Maladies by Jhumpa Lahiri"
    assert results["winners"][1] == "A Matter of Profit by Hilari Bell"
    assert results["losers"][0] == "Lirael by Garth Nix"
    assert results["losers"][1] == "Out of the Silent Planet by C. S. Lewis"


def test_matchup_even_json(timeline_even, monkeypatch):

    random.seed(a=1, version=2)

    cli_inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))

    results = matchup(timeline_even)
    timeline = results["timeline_winners"]

    assert timeline[0]["title"]["text"] == "Interpreter of Maladies"
    assert timeline[1]["title"]["text"] == "A Matter of Profit"
    assert timeline[0]["author"] == "Jhumpa Lahiri"
    assert timeline[1]["author"] == "Hilari Bell"
