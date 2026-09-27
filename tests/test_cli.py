import json

import pytest

import cyberjev
from cyberjev.__main__ import main


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert cyberjev.__version__ in capsys.readouterr().out


def test_use_local_folder_then_current(isolated_home, tiny_model_dir, capsys):
    main(["use", str(tiny_model_dir)])
    main(["current"])
    out = capsys.readouterr().out
    assert str(tiny_model_dir.resolve()) in out


def test_use_reset(isolated_home, tiny_model_dir, capsys):
    main(["use", str(tiny_model_dir)])
    main(["use", "--reset"])
    assert f"using {cyberjev.DEFAULT_VERSION}" in capsys.readouterr().out


def test_http_attack_json(tiny_model_dir, capsys):
    main(["http_attack", "--model", str(tiny_model_dir), "--json",
          "GET /login?user=admin' HTTP/1.1", "GET /search?q=shoes HTTP/1.1"])
    result = json.loads(capsys.readouterr().out)
    assert len(result) == 2
    assert set(result[0]) == {"safe", "attack"}


def test_single_input_gives_single_result(tiny_model_dir, capsys):
    main(["phishing_url", "--model", str(tiny_model_dir), "--json", "http://example.com/login"])
    assert set(json.loads(capsys.readouterr().out)) == {"legitimate", "phishing"}


def test_decide_json(tiny_model_dir, capsys):
    main(["decide", "--model", str(tiny_model_dir), "--json", "--question", "Which topic?",
          "-o", "history", "-o", "cooking", "--state", "GET /search HTTP/1.1"])
    result = json.loads(capsys.readouterr().out)
    assert set(result) == {"history", "cooking"}
    assert sum(result.values()) == pytest.approx(1.0, abs=1e-5)


def test_list_offline_shows_local_folder(tiny_model_dir, isolated_home, capsys):
    main(["list", "--offline", "--local", str(tiny_model_dir.parent)])
    out = capsys.readouterr().out
    assert tiny_model_dir.name in out
    assert "selected:" in out
