import pytest
import requests

from src.api.hh import HeadHunterAPI


@pytest.fixture
def mock_api(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '{"items": [{"id": "1", "name": "Test Job", "alternate_url": "http://hh.ru/1", "salary": {"from": 100000}, "snippet": {"requirement": "req", "responsibility": "resp"}, "employer": {"name": "Test Employer"}}]}'

            def json(self):
                return eval(self.text)

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    return HeadHunterAPI()