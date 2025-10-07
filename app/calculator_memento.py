from dataclasses import dataclass
import pandas as pd

@dataclass
class HistoryMemento:
    df: pd.DataFrame

class Caretaker:
    def __init__(self):
        self._undos: list[HistoryMemento] = []
        self._redos: list[HistoryMemento] = []

    def push_undo(self, m: HistoryMemento): self._undos.append(m)
    def push_redo(self, m: HistoryMemento): self._redos.append(m)
    def pop_undo(self): return self._undos.pop() if self._undos else None
    def pop_redo(self): return self._redos.pop() if self._redos else None
    def clear_redo(self): self._redos.clear()
    def has_undo(self) -> bool: return bool(self._undos)
    def has_redo(self) -> bool: return bool(self._redos)
