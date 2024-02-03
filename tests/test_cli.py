"""
Functions to test the CLI interface
"""

from libby_bracket.cli import get_matchup_input


def test_get_matchup_input_valid(monkeypatch):
    """Test CLI where first input is valid.
    """
    cli_inputs = iter(["3"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))
    assert get_matchup_input() == 3

def test_get_matchup_input_invalid(monkeypatch):
    """Test CLI where first input is invalid but second is valid.
    """
    cli_inputs = iter(["5", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(cli_inputs))
    assert get_matchup_input() == 2