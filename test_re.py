import pytest
import re


def check_version_format(version_string):
    version_pattern = re.compile(
        r"^0\.202[1-9]\.(1[0-2]|[1-9])\.(3[01]|[12][0-9]|[1-9])$"
    )
    return False if not version_pattern.match(version_string) else True


def test_valid_version_numbers():
    test_strings = [
        "0.2023.12.31",
        "0.2023.8.9",
        "0.2023.1.31",
        "0.2023.12.3",
        "0.2029.9.15",
    ]
    for version in test_strings:
        assert check_version_format(version) is True, f"Failed for {version}"


def test_invalid_version_numbers():
    test_strings = [
        "2023.12.31",
        "0.202.12.31",
        "0.20.23.12.31",
        "0.2023.13.31",
        "0.2023.01.31",
        "0.2023.12.01",
        "0.2023.09.05",
        "0.2023.7.05",
        "0.2023.13.3",
        "0.2023.99.99",
    ]
    for version in test_strings:
        assert check_version_format(version) is False, f"Failed for {version}"


if __name__ == "__main__":
    pytest.main()
