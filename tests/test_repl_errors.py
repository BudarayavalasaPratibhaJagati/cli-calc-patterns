from io import StringIO
from app.calculator_repl import main

def run(cmds):
    stdin = StringIO("\n".join(cmds) + "\n")
    out = StringIO()
    main(stdin=stdin, stdout=out)
    return out.getvalue()

def test_repl_errors_and_nonempty_history(tmp_path, monkeypatch):
    monkeypatch.setenv("CALC_AUTOSAVE_PATH", str(tmp_path/"auto.csv"))
    out = run([
        "+ 2 3",     # add something to make history non-empty
        "history",   # prints non-empty branch
        "/ 1 0",     # division by zero -> CalculatorError path
        "",          # blank line -> ValidationError path -> "error:"
        "exit"
    ])
    assert "5.0" in out
    assert "error:" in out
    assert "timestamp" in out and "expr" in out and "result" in out
