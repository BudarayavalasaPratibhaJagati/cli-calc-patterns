import pytest
from app.exceptions import ConfigError

def test_config_invalid_paths(monkeypatch):
    monkeypatch.setenv("CALC_AUTOSAVE_PATH", "")
    monkeypatch.setenv("CALC_HISTORY_PATH", "")
    from importlib import reload
    import app.calculator_config as cc
    reload(cc)  # ensure it reads env again
    with pytest.raises(ConfigError):
        cc.load_config()
