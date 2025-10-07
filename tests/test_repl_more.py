from io import StringIO
from app.calculator_repl import main

def run(cmds):
    stdin = StringIO("\n".join(cmds) + "\n")
    out = StringIO()
    main(stdin=stdin, stdout=out)
    return out.getvalue()

def test_repl_branches(tmp_path, monkeypatch):
    monkeypatch.setenv("CALC_AUTOSAVE_PATH", str(tmp_path/"auto.csv"))
    # start with history when empty, unknown cmd, help alias h, clear, do calc, save/load, exit
    out = run(["history", "xyz", "h", "clear", "+ 1 2", "save", "load", "exit"])
    assert "(empty)" in out
    assert "unknown command" in out
    assert "Commands:" in out
    assert "cleared." in out
    assert "3.0" in out
    assert "saved to" in out
    assert "loaded from" in out
