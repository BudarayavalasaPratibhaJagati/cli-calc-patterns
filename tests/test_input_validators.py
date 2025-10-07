import pytest
from app.input_validators import parse_command, parse_two_numbers
from app.exceptions import ValidationError

def test_parse_command_ok():
    assert parse_command(" + 2 3 ") == ["+", "2", "3"]

def test_parse_command_empty():
    with pytest.raises(ValidationError):
        parse_command("   ")

def test_parse_two_numbers_ok():
    assert parse_two_numbers(["+", "2", "3"]) == (2.0, 3.0)

def test_parse_two_numbers_bad():
    with pytest.raises(ValidationError):
        parse_two_numbers(["+","x","3"])
