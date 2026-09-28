"""Decision definitions: question and option set for each typed security decision."""

import re
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


# Content-negotiation headers: the same few values on every request, attack or not.
# Dropping them keeps inputs short; headers that can carry payloads (User-Agent, Referer,
# Cookie, Host, X-*, ...) are kept.
BOILERPLATE_HEADERS = {"accept", "accept-charset", "accept-encoding", "accept-language",
                       "cache-control", "connection", "content-length", "dnt", "keep-alive",
                       "pragma", "priority", "te", "upgrade-insecure-requests"}
_REQUEST_LINE = re.compile(r"^[A-Z]{3,7} \S")
_ABSOLUTE_URL = re.compile(r"^([A-Z]+ )https?://[^/\s]+")


def _boilerplate(name: str) -> bool:
    name = name.strip().lower()
    return name in BOILERPLATE_HEADERS or name.startswith(("sec-ch-", "sec-fetch-"))


def normalize_http(request: str) -> str:
    """Canonical text for an HTTP request or a bare payload. Training data and inference
    both go through this.

    A full request ("GET /x HTTP/1.1\nHeader: v\n\nbody") becomes the request line (without
    scheme and host), the non-boilerplate headers, then "body: ...", URL-decoded.
    Anything else (a bare payload) is just URL-decoded.
    """
    request = request.replace("\r\n", "\n")
    if not _REQUEST_LINE.match(request):
        return unquote_plus(request)
    head, _, body = request.partition("\n\n")
    first, *header_lines = head.split("\n")
    lines = [_ABSOLUTE_URL.sub(r"\1", first)]
    for h in header_lines:
        name, sep, _ = h.partition(":")
        if h.strip() and not (sep and _boilerplate(name)):
            lines.append(h)
    if body.strip():
        lines.append(f"body: {body}")
    return unquote_plus("\n".join(lines))
