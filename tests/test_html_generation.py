import pytest

from generate_html_layout import *

def test_generator():
    generator = HTMLGenerator()
    f = open('test_config.yaml')

    interface = read_layout_config(f)

    generator.generate(interface)
    assert len(generator.styles) == 5
    assert len(generator.bodies) == 5
