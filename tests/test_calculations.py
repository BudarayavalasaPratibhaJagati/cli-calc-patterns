from app.calculation import Calculation
from app.operations import Add

def test_calc_runs():
    c = Calculation(2, 3, Add())
    assert c.run() == 5
