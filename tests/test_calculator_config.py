def test_config_defaults(monkeypatch):
    monkeypatch.delenv("CALC_AUTOSAVE", raising=False)
    from app.calculator_config import load_config
    c = load_config()
    assert c.autosave is True
    assert c.autosave_path.endswith(".csv")
