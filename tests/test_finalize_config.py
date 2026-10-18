"""Regression tests for finalize configuration selection."""

import yaml

from utils.config_loader import load_finalize_config


def test_finalize_honors_hound_config_environment_variable(tmp_path, monkeypatch):
    config_path = tmp_path / "subscription.yaml"
    config_path.write_text(yaml.safe_dump({
        "openai": {"api_key_env": "HOUND_GATEWAY_TOKEN", "base_url": "http://127.0.0.1:4000/v1"},
        "models": {"finalize": {"provider": "openai", "model": "openai-codex/gpt-6-luna"}},
    }))
    monkeypatch.setenv("HOUND_CONFIG", str(config_path))

    config = load_finalize_config()

    assert config["openai"]["api_key_env"] == "HOUND_GATEWAY_TOKEN"
    assert config["openai"]["base_url"] == "http://127.0.0.1:4000/v1"
    assert config["models"]["finalize"]["model"] == "openai-codex/gpt-6-luna"


def test_finalize_cli_overrides_keep_other_subscription_config(tmp_path, monkeypatch):
    config_path = tmp_path / "subscription.yaml"
    config_path.write_text(yaml.safe_dump({
        "openai": {"api_key_env": "HOUND_GATEWAY_TOKEN"},
        "models": {"finalize": {"provider": "openai", "model": "openai-codex/gpt-6-luna"}},
    }))
    monkeypatch.setenv("HOUND_CONFIG", str(config_path))

    config = load_finalize_config(platform="mock", model="test-model")

    assert config["openai"]["api_key_env"] == "HOUND_GATEWAY_TOKEN"
    assert config["models"]["finalize"] == {"provider": "mock", "model": "test-model"}
