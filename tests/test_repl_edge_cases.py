from io import StringIO
import pytest
from app import calculator_repl as repl

def run_io(text: str) -> str:
    stdin = StringIO(text)
    out = StringIO()
    repl.main(stdin=stdin, stdout=out)
    return out.getvalue()

def test_repl_eof_breaks():
    # empty input -> readline() returns "" -> loop breaks
    out = run_io("")
    assert "Calculator REPL" in out  # banner printed

def test_repl_fatal(monkeypatch):
    # make OperationFactory.create raise an unexpected RuntimeError
    def boom(_cmd):  # _cmd like "+"
        raise RuntimeError("boom")
    monkeypatch.setattr(repl.OperationFactory, "create", boom, raising=True)

    out = run_io("+ 1 2\n")
    assert "fatal:" in out
