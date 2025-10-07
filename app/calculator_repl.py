"""
Author: Rizmi Sowdhagar  Date: 2025-10-07
A tiny but complete REPL that wires Strategy, Factory, Observer, Memento, Facade, and pandas history.
"""
from __future__ import annotations
import sys
from typing import Callable
from .calculator_config import load_config
from .history import History
from .operations import OperationFactory
from .calculation import Calculation
from .input_validators import parse_command, parse_two_numbers
from .exceptions import CalculatorError

def make_autosave_observer(path: str) -> Callable:
    def _obs(df):
        df.to_csv(path, index=False)
    return _obs

HELP_TEXT = """Commands:
  + a b  | - a b | * a b | / a b | ^ a b | root a b
  history | undo | redo | save <path> | load <path> | clear | help | exit
"""

def main(stdin=None, stdout=None):
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout

    cfg = load_config()
    hist = History()

    if cfg.autosave:
        hist.attach(make_autosave_observer(cfg.autosave_path))

    print("Calculator REPL. Type 'help' for commands.", file=stdout)

    while True:
        try:
            print("> ", end="", file=stdout)
            line = stdin.readline()
            if not line:
                break

            tokens = parse_command(line)
            cmd = tokens[0].lower()

            if cmd in {"help", "h"}:
                print(HELP_TEXT, file=stdout)
                continue

            if cmd == "exit":
                print("bye!", file=stdout)
                break

            if cmd == "history":
                if hist.df.empty:
                    print("(empty)", file=stdout)
                else:
                    print(hist.df.to_string(index=False), file=stdout)
                continue

            if cmd == "clear":
                hist.df = hist.df.iloc[0:0]
                print("cleared.", file=stdout)
                continue

            if cmd == "undo":
                print("undone." if hist.undo() else "nothing to undo.", file=stdout)
                continue

            if cmd == "redo":
                print("redone." if hist.redo() else "nothing to redo.", file=stdout)
                continue

            if cmd == "save":
                path = tokens[1] if len(tokens) > 1 else cfg.history_path
                hist.save_csv(path)
                print(f"saved to {path}", file=stdout)
                continue

            if cmd == "load":
                path = tokens[1] if len(tokens) > 1 else cfg.history_path
                hist.load_csv(path)
                print(f"loaded from {path}", file=stdout)
                continue

            if cmd in {"+","-","*","/","^","pow","power","root","add","sub","mul","div"}:
                a, b = parse_two_numbers(tokens)
                op = OperationFactory.create(cmd)
                calc = Calculation(a=a, b=b, op=op)
                result = calc.run()
                expr = f"{cmd} {a} {b}"
                hist.record(expr, result)
                print(result, file=stdout)
                continue

            print("unknown command. type 'help'.", file=stdout)

        except CalculatorError as ce:
            print(f"error: {ce}", file=stdout)
        except Exception as e:  # last-resort guard
            print(f"fatal: {e}", file=stdout)

if __name__ == "__main__":  # pragma: no cover
    main()
