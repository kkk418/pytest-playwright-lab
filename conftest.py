import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    ui_base_url: str = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
    api_base_url: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    sauce_username: str = os.getenv("SAUCE_USERNAME", "standard_user")
    sauce_password: str = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    headless: bool = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()


@pytest.fixture(scope="session")
def api_client(settings: Settings):
    import httpx

    with httpx.Client(base_url=settings.api_base_url, timeout=15.0) as client:
        yield client

