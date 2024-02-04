"""
Functions to test the JSON parsers
"""

from libby_bracket.parse_libby import get_json_from_file


def test_get_json_from_file_type():

    artifact_path = "tests/artifacts/borrowed_only_even.json"

    libby_json = get_json_from_file(artifact_path)

    assert isinstance(libby_json, dict)


def test_get_json_from_file_value():

    artifact_path = "tests/artifacts/borrowed_only_even.json"

    libby_json = get_json_from_file(artifact_path)

    assert libby_json["version"] == 1
    assert libby_json["timeline"][1]["title"]["text"] == "A Matter of Profit"
    assert libby_json["timeline"][2]["activity"] == "Borrowed"
