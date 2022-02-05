# you should install PyYAML/pyyaml :)

import yaml

user_config = dict()
with open("user_config.yaml", 'r') as yaml_in:
    user_config = yaml.safe_load(yaml_in)
