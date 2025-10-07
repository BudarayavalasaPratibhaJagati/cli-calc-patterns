from app.exceptions import CalculatorError, ValidationError, OperationError, ConfigError

def test_exception_hierarchy():
    assert issubclass(ValidationError, CalculatorError)
    assert issubclass(OperationError, CalculatorError)
    assert issubclass(ConfigError, CalculatorError)
