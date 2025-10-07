import pytest
from app.input_validators import parse_two_numbers
from app.exceptions import ValidationError

def test_parse_two_numbers_too_few_tokens():
    with pytest.raises(ValidationError):
        parse_two_numbers(["+", "2"])  # needs two numbers
