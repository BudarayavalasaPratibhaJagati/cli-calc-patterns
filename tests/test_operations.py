import pytest
from app.operations import OperationFactory, OperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("+", 2, 3, 5),
    ("-", 5, 2, 3),
    ("*", 4, 3, 12),
    ("/", 8, 2, 4),
    ("^", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_ops(op, a, b, expected):
    strat = OperationFactory.create(op)
    assert strat.execute(a, b) == pytest.approx(expected)

def test_div_zero():
    with pytest.raises(OperationError):
        OperationFactory.create("/").execute(1, 0)

def test_unknown():
    with pytest.raises(OperationError):
        OperationFactory.create("%")
