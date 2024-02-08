import pytest


@pytest.fixture
def yaml_config_file():
  with open('tests/fixtures/config_file.yml') as config:
    yield config


def test_load_yaml(yaml_config_file):
  pass
