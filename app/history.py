from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import Callable, List
from .calculator_memento import HistoryMemento, Caretaker

Observer = Callable[[pd.DataFrame], None]

class History:
    def __init__(self):
        self.df = pd.DataFrame(columns=["timestamp", "expr", "result"])
        self._observers: List[Observer] = []
        self._caretaker = Caretaker()

    def attach(self, fn: Observer):
        if fn not in self._observers:
            self._observers.append(fn)

    def notify(self):
        for fn in list(self._observers):
            fn(self.df)

    def snapshot(self) -> HistoryMemento:
        return HistoryMemento(self.df.copy(deep=True))

    def restore(self, m: HistoryMemento):
        self.df = m.df.copy(deep=True)

    # --- fixed undo/redo logic ---
    def record(self, expr: str, result: float):
        self._caretaker.push_undo(self.snapshot())
        self._caretaker.clear_redo()
        self.df.loc[len(self.df)] = [datetime.now().isoformat(timespec="seconds"), expr, result]
        self.notify()

    def undo(self) -> bool:
        if not self._caretaker.has_undo():
            return False
        self._caretaker.push_redo(self.snapshot())
        m = self._caretaker.pop_undo()
        self.restore(m)
        self.notify()
        return True

    def redo(self) -> bool:
        if not self._caretaker.has_redo():
            return False
        self._caretaker.push_undo(self.snapshot())
        m = self._caretaker.pop_redo()
        self.restore(m)
        self.notify()
        return True

    def save_csv(self, path: str):
        self.df.to_csv(path, index=False)

    def load_csv(self, path: str):
        self._caretaker.push_undo(self.snapshot())
        self._caretaker.clear_redo()
        self.df = pd.read_csv(path)
        self.notify()
