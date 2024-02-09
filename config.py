from os import path
import yaml


class Members:
  def __init__(self, selfName, memberNames):
    self.selfName = selfName
    self.memberNames = memberNames

  def from_dict(members_dict):
    return Members(members_dict['self'], members_dict['others'])

  def to_dict(self):
    return {
      'self': self.selfName,
      'others': self.memberNames
    }

  def copy(self):
    return Members(self.selfName, self.memberNames.copy())


class Config:
  def __init__(self, members):
    self.members = members

  def from_dict(configDict):
    return Config(
      Members.from_dict(configDict['members'])
    )

  def to_dict(self):
    return {
      'members': self.members.to_dict()
    }

  def copy(self):
    return Config(self.members.copy())

  def load(filepath):
    config = None
    if path.exists(filepath):
      with open(filepath, encoding='UTF-8') as file:
        config = yaml.full_load(file)
    if config != None:
      return Config.from_dict(config)
    else:
      return Config(Members('', []))

  def save(self, filepath):
    with open(filepath, 'w+', encoding='UTF-8') as file:
      yaml.safe_dump(self.to_dict(), file, sort_keys=False)
