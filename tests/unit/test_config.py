import pytest
from Backend.config import Config


def test_default_config_values():
    assert Config.SQLALCHEMY_DATABASE_URI is not None
    assert Config.SECRET_KEY is not None


def test_ssl_validation_passes_for_postgres(monkeypatch):
    monkeypatch.setenv("ENABLE_SSL", "true")
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql://user:pass@localhost/db"
    )

    Config.ENABLE_SSL = True
    Config.SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/db"

    Config.validate_ssl_config()


def test_ssl_validation_fails_for_sqlite(monkeypatch):
    monkeypatch.setenv("ENABLE_SSL", "true")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")

    Config.ENABLE_SSL = True
    Config.SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"

    with pytest.raises(ValueError):
        Config.validate_ssl_config()
