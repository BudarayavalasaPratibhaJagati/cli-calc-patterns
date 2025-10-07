from dataclasses import dataclass
import os
from dotenv import load_dotenv
from .exceptions import ConfigError

load_dotenv()

@dataclass(frozen=True)
class Config:
    autosave: bool
    autosave_path: str
    history_path: str

def load_config() -> Config:
    autosave = os.getenv("CALC_AUTOSAVE", "true").lower() in {"1", "true", "yes"}
    autosave_path = os.getenv("CALC_AUTOSAVE_PATH", "autosave.csv")
    history_path = os.getenv("CALC_HISTORY_PATH", "history.csv")
    if not autosave_path or not history_path:
        raise ConfigError("Invalid paths in environment.")
    return Config(autosave=autosave, autosave_path=autosave_path, history_path=history_path)
