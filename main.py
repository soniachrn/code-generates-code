import argparse

from autolayout import autolayout
from config_reader import read_layout_config
from layout_generator import generate_html_layout


def read_cli_args():
     parser = argparse.ArgumentParser(description='Code generates code')
     parser.add_argument('--config', help='Configuration file path', required=True)
     parser.add_argument('--output', help='HTML output file', default='layout.html')
     return parser.parse_args()


def main():
    args = read_cli_args()

    layout = read_layout_config(args.config)
    autolayout(layout)
    generate_html_layout(layout, args.output)


if __name__ == '__main__':
    main()

