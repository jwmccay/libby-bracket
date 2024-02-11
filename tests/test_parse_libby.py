"""
Functions to test the JSON parsers
"""

import pytest

from libby_bracket.parse_libby import (
    get_json_from_file,
    cleanup_downloaded_timeline)


@pytest.fixture
def timeline_even():

    artifact_path = "tests/artifacts/borrowed_only_even.json"
    libby_json = get_json_from_file(artifact_path)

    return libby_json["timeline"]


@pytest.fixture
def timeline_duplicates():

    artifact_path = "tests/artifacts/duplicates.json"
    libby_json = get_json_from_file(artifact_path)

    return libby_json["timeline"]


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


def test_cleanup_downloaded_timeline(timeline_duplicates):
    """Check function that cleans up a downloaded timeline. The example
    should have 6 entries with one duplicate and one non-borrow event.
    """

    timeline_new, stats = cleanup_downloaded_timeline(
        timeline_duplicates
    )

    assert stats["original_count"] == 6
    assert stats["duplicate_count"] == 1
    assert stats["nonborrowed_count"] == 1
    assert stats["new_count"] == 4
    assert len(timeline_new) == stats["new_count"]
