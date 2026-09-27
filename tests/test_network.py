"""End-to-end tests against the published weights. Opt in with CYBERJEV_NETWORK_TESTS=1.

Every released version must stay listed and loadable, not just the newest one.
"""

import os

import pytest

import cyberjev

RELEASED: dict[str, str] = {}  # Hub tag -> version in cyberjev_config.json (none published yet)

pytestmark = [
    pytest.mark.network,
    pytest.mark.skipif(os.environ.get("CYBERJEV_NETWORK_TESTS") != "1",
                       reason="set CYBERJEV_NETWORK_TESTS=1 to download the real model"),
]


@pytest.fixture(scope="module", params=sorted(RELEASED))
def real_decider(request):
    return request.param, cyberjev.load(request.param, device="cpu")


def test_all_released_versions_are_listed_on_the_hub():
    models, online = cyberjev.list_models()
    assert online
    assert set(RELEASED) <= {m.name for m in models}


def test_default_version_is_released():
    assert cyberjev.DEFAULT_VERSION in RELEASED


def test_real_model_metadata(real_decider):
    tag, d = real_decider
    assert d.version == RELEASED[tag]
    assert set(d.temperatures) >= {"http_attack"}


def test_real_model_decisions(real_decider):
    _, d = real_decider
    attack, safe = d.http_attack(["GET /login?user=admin' OR '1'='1' -- HTTP/1.1",
                                  "GET /products?category=shoes&page=2 HTTP/1.1"])
    assert attack["attack"] > 0.5
    assert safe["safe"] > 0.5
