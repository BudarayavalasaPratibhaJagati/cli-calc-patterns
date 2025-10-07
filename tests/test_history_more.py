from app.history import History

def test_history_undo_redo_nothing():
    h = History()
    assert h.undo() is False
    assert h.redo() is False

def test_history_load_clears_redo(tmp_path):
    h = History()
    h.record("a", 1)
    p = tmp_path / "h.csv"
    h.save_csv(str(p))
    h.record("b", 2)
    assert h.undo() is True        # one step back, redo available
    h.load_csv(str(p))              # load should clear redo chain
    assert h.redo() is False
