import time

from autolayout import autolayout
from config_reader import read_layout_config
from layout_generator import generate_html_layout


def test_perf():
    config_filename = 'tests/data/performance_test.yaml'

    start = time.time()

    layout = read_layout_config(config_filename)
    autolayout(layout)
    generate_html_layout(layout, "out.txt")

    end = time.time()
    assert end - start < 60

