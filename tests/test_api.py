import pytest
import requests

from src.api.hh import HeadHunterAPI


@pytest.fixture
def api():
    return HeadHunterAPI()


def test_connect_error(mocker, api):
    mocker.patch("requests.get", side_effect=requests.RequestException("Connection error"))
    with pytest.raises(ConnectionError):
        api.connect()


def test_get_vacancies_error(mocker, api):
    mocker.patch("requests.get", side_effect=requests.RequestException("API error"))
    with pytest.raises(ConnectionError):  # Изменяем на ConnectionError
        api.get_vacancies("test")


def test_get_vacancies_mock(mocker):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '{"items": [{"id": "1", "name": "Test Job", "alternate_url": "http://hh.ru/1", "salary": {"from": 100000}, "snippet": {"requirement": "req", "responsibility": "resp"}, "employer": {"name": "Test Employer"}}]}'

            def json(self):
                return eval(self.text)

        return MockResponse()

    mocker.patch("requests.get", mock_get)
    api = HeadHunterAPI()
    data = api.get_vacancies("test", 1)
    assert len(data) == 1
    assert data[0]["name"] == "Test Job"