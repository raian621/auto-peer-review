from gui import start_gui
from config import Config


if __name__ == '__main__':
  config = Config.load('config.yml')
  start_gui(config)
