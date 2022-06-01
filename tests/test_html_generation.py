import pytest

from layout_generator import *
from config_reader import read_layout_config

def test_generator():
    generator = HTMLGenerator()
    f = 'tests/data/test_config_simple.yaml'

    interface = read_layout_config(f)

    generator.generate(interface)
    assert len(generator.styles) == 5
    assert len(generator.bodies) == 5

