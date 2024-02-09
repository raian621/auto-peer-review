import pytest
import yaml
import tempfile
from config import Config


@pytest.fixture
def yaml_config_dict():
  with open('tests/fixtures/config_file.yml') as config:
    yield yaml.full_load(config)


def test_load_config_from_file():
  config = Config.load('tests/fixtures/config_file.yml')
  assert config.members.selfName == 'Your Name'
  assert config.members.memberNames[0] == 'Member One'
  assert config.members.memberNames[1] == 'Member Two'
  assert config.members.memberNames[2] == 'Member Three'


def test_load_config_from_dict(yaml_config_dict):
  config = Config.from_dict(yaml_config_dict)
  assert config.members.selfName == 'Your Name'
  assert config.members.memberNames[0] == 'Member One'
  assert config.members.memberNames[1] == 'Member Two'
  assert config.members.memberNames[2] == 'Member Three'


def test_save_config():
  config = Config.load('tests/fixtures/config_file.yml')
  tmpFile = tempfile.NamedTemporaryFile()
  config.save(tmpFile.name)
  configCopy = Config.load(tmpFile.name)

  assert config.members.selfName == configCopy.members.selfName
  for i, name in enumerate(config.members.memberNames):
    assert name == configCopy.members.memberNames[i]

  tmpFile.close()  # deletes file on close


def test_copy_config(yaml_config_dict):
  config = Config.from_dict(yaml_config_dict)
  copy = config.copy()

  assert copy.members.selfName == config.members.selfName
  for i, name in enumerate(config.members.memberNames):
    assert copy.members.memberNames[i] == name
