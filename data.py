from os import path

DOCX_TEMPLATE_PATH = path.abspath(
  path.join(path.dirname(__file__), 'assets/data/peer_eval_template.docx')
)

CONFIG_PATH = path.abspath(
  path.join(path.dirname(__file__), 'config.yml')
)