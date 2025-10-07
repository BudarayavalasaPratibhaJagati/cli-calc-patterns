import pytest
from app.calculation import Calculation
from app.operations import Div
from app.exceptions import OperationError

def test_calculation_wraps_operation_error():
    c = Calculation(1, 0, Div())
    with pytest.raises(OperationError):
        c.run()
