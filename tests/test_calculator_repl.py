from io import StringIO
from app.calculator_repl import main

def run(lines: list[str]) -> str:
    stdin = StringIO("\n".join(lines)+ "\n")
    out = StringIO()
    main(stdin=stdin, stdout=out)
    return out.getvalue()

def test_repl_basic_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("CALC_AUTOSAVE_PATH", str(tmp_path/"auto.csv"))
    out = run(["+ 2 3", "history", "undo", "redo", "save", "help", "exit"])
    assert "5.0" in out
    assert "history" in out.lower()
    assert "undone." in out
    assert "redone." in out
    assert "saved to" in out
    assert "Commands:" in out
