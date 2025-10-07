class CalculatorError(Exception):
    """Base calculator error."""

class ConfigError(CalculatorError):
    """Bad or missing configuration."""

class ValidationError(CalculatorError):
    """Bad user input."""

class OperationError(CalculatorError):
    """Invalid operation (e.g., divide by zero)."""
