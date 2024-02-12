from gui import start_gui
from config import Config
from data import CONFIG_PATH


if __name__ == '__main__':
  config = Config.load(CONFIG_PATH)
  start_gui(config)
