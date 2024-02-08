from gui import start_gui
from config import load_config, save_config

if __name__ == '__main__':
  config = load_config('config.yml')
  save_config(config, 'config-copy.yml')
  print(config)
  start_gui(config)
