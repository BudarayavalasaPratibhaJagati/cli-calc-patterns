from abc import ABC, abstractmethod
from .exceptions import OperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:  # pragma: no cover (abstract)
        ...

class Add(Operation):
    def execute(self, a, b): return a + b

class Sub(Operation):
    def execute(self, a, b): return a - b

class Mul(Operation):
    def execute(self, a, b): return a * b

class Div(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero")
        return a / b

class Pow(Operation):
    def execute(self, a, b): return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Zeroth root undefined")
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of negative number")
        return a ** (1.0 / b)

class OperationFactory:
    _map = {
        "+": Add, "add": Add,
        "-": Sub, "sub": Sub,
        "*": Mul, "mul": Mul,
        "/": Div, "div": Div,
        "^": Pow, "pow": Pow, "power": Pow,
        "root": Root
    }
    @classmethod
    def create(cls, token: str) -> Operation:
        key = str(token).strip().lower()
        if key not in cls._map:
            raise OperationError(f"Unknown operation: {token}")
        return cls._map[key]()
