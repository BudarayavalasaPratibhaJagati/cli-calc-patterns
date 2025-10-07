import pytest
from app.operations import OperationFactory, OperationError

def test_root_zeroth():
    with pytest.raises(OperationError):
        OperationFactory.create("root").execute(9, 0)

def test_root_even_negative():
    with pytest.raises(OperationError):
        OperationFactory.create("root").execute(-9, 2)
