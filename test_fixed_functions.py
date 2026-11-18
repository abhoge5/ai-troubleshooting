import pytest

from buggy_functions import (
    average_response_time,
    format_alert_summary,
    get_alert_owner,
)


@pytest.mark.parametrize(
    "alert_count, severity, expected",
    [
        (3, "critical", "There are 3 critical alerts active."),
        (0, "warning", "There are 0 warning alerts active."),
        (1, "info", "There are 1 info alerts active."),
    ],
)
def test_format_alert_summary(alert_count, severity, expected):
    assert format_alert_summary(alert_count, severity) == expected


@pytest.mark.parametrize(
    "alert, team_directory, expected",
    [
        ({"owner": "oncall"}, {"oncall": "Alice"}, "Alice"),
        ({}, {"oncall": "Alice"}, None),
        ({"owner": "unknown"}, {"oncall": "Alice"}, None),
        ({"owner": "oncall"}, {}, None),
    ],
)
def test_get_alert_owner(alert, team_directory, expected):
    assert get_alert_owner(alert, team_directory) == expected


@pytest.mark.parametrize(
    "response_times, expected",
    [
        ([], 0.0),
        ([5], 5.0),
        ([2, 4, 6], 4.0),
        ([1, 2], 1.5),
        ([0, 0], 0.0),
    ],
)
def test_average_response_time(response_times, expected):
    result = average_response_time(response_times)
    assert isinstance(result, float)
    assert result == pytest.approx(expected)