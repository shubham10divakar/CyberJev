"""Decision definitions: question and option set for each typed security decision."""

from dataclasses import dataclass
from urllib.parse import unquote_plus

SCHEMA_VERSION = "0.1"


@dataclass(frozen=True)
class Decision:
    name: str
    kind: str  # "choice" | "noul" | "score"
    question: str
    options: tuple[str, ...]


DECISIONS: dict[str, Decision] = {
    "http_attack": Decision(
        name="http_attack",
        kind="noul",
        question="Is this HTTP request a web attack "
                 "(SQL injection, XSS, path traversal, command injection)?",
        options=("safe", "attack"),
    ),
    "prompt_injection": Decision(
        name="prompt_injection",
        kind="noul",
        question="Is this text trying to override an AI model's instructions or jailbreak it?",
        options=("safe", "injection"),
    ),
    "phishing_url": Decision(
        name="phishing_url",
        kind="noul",
        question="Is this URL phishing or malicious?",
        options=("legitimate", "phishing"),
    ),
}


def normalize_http(request: str) -> str:
    """URL-decode a request line (+ body). Training data and inference both go through this."""
    return unquote_plus(request)
