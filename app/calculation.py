from dataclasses import dataclass
from .operations import Operation
from .exceptions import OperationError

@dataclass
class Calculation:
    a: float
    b: float
    op: Operation

    def run(self) -> float:
        try:
            return self.op.execute(self.a, self.b)
        except Exception as exc:  # EAFP
            raise OperationError(str(exc)) from exc
