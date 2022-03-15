import pytest

from config_reader import read_layout_config

def test_read():
    f = 'tests/data/test_config_simple.yaml'

    interface = read_layout_config(f)
    assert len(interface.children) == 3

    assert interface.children[0].label.text == "Your name"
    assert interface.children[0].textfield.text == "John"
    assert interface.children[0].button.color == "green"

    assert interface.children[1].image.url == "my.image/url"

    assert interface.children[2].text == "Nice image huh?"

