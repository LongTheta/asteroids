"""Load and save high score to file."""
import json
from pathlib import Path

from constants import HIGH_SCORE_FILE


def load_high_score():
    try:
        path = Path(HIGH_SCORE_FILE)
        if path.exists():
            with open(path) as f:
                data = json.load(f)
                return data.get("high_score", 0)
    except (json.JSONDecodeError, IOError):
        pass
    return 0


def save_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            json.dump({"high_score": score}, f)
    except IOError:
        pass
