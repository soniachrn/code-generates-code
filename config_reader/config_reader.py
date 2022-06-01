import yaml

from interface.interface import *


def _get_config_yaml_root(input_yaml_file_path: str) -> dict:
    with open(input_yaml_file_path) as input_yaml_file:
        try:
            return yaml.safe_load(input_yaml_file)
        except yaml.YAMLError as exc:
            print(f'Error while trying to read yaml config {input_yaml_file_path}:')
            print(exc)
            exit(1)


"""   Example config

interface:
  width: 600
  height: 400
  children:
    - group:
        children:
          - label
              text: Your name
          - textfield
              placeholder: John
          - button
              text: Greet
    - image:
        url: "my.image/url"
    - text:
        text: "Nice image huh?"

"""

def read_layout_config(input_yaml_file_path: str) -> Interface:
    root: dict = _get_config_yaml_root(input_yaml_file_path) 
    assert('interface' in root)
    assert(len(root) == 1)

    return Interface(root['interface'])

