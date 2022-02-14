import pytest

from config_reader import *

def test_read():
    f = open('test_config.yaml')

    interface = read_layout_config(f)
    assert len(interface.children) == 3

    assert interface.children[0].label.text == "Your name"
    assert interface.children[0].textfield.text == "John"
    assert interface.children[0].button.color == "green"

    assert interface.children[1].image.url == "my.image/url"

    assert interface.children[2].text == "Nice image huh?"