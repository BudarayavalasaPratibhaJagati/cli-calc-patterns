from app.history import History

def test_history_record_and_save(tmp_path):
    h = History()
    h.record("+ 1 2", 3)
    assert len(h.df) == 1
    p = tmp_path/"h.csv"
    h.save_csv(str(p))
    assert p.exists()

def test_undo_redo():
    h = History()
    h.record("x", 1)
    h.record("y", 2)
    assert h.undo() is True
    assert len(h.df) == 1
    assert h.redo() is True
    assert len(h.df) == 2
