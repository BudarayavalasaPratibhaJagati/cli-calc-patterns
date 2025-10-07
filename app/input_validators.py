from .exceptions import ValidationError

def parse_command(line: str) -> list[str]:
    if not line or not line.strip():
        raise ValidationError("Empty input")
    return line.strip().split()

def parse_two_numbers(tokens: list[str]) -> tuple[float, float]:
    if len(tokens) < 3:
        raise ValidationError("Need two numbers, e.g., '+ 2 3'")
    try:
        a = float(tokens[1])
        b = float(tokens[2])
    except ValueError as e:
        raise ValidationError("Numbers must be numeric") from e
    return a, b
