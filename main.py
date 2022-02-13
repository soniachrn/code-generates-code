import argparse

from autolayout import autolayout
from config_reader import read_layout_config
from interface import Interface
from layout_generator import generate_html_layout


def read_cli_args():
    parser = argparse.ArgumentParser(description='Code generates code')
    parser.add_argument('--config', help='Configuration file path', required=True)
    parser.add_argument('--output', help='HTML output file', default='layout.html')
    return parser.parse_args()


# Usage
# python3 main.py --config config.yaml

def main():
    args = read_cli_args()

    interface: Interface = read_layout_config(args.config)
        
    # Принтилка результата парсинга текущего конфига
    print('interface:', interface)
    print('i.width, i.height, i.pos:',interface.width, interface.height, interface.position)
    print('group.label.text:', interface.children[0].children[0].text)
    print('image.url:', interface.children[1].url)
    print('text.text:', interface.children[2].text)
    print('text2.text:', interface.children[3].text)

    # layed_out_interface: Interface = autolayout(interface)
    # generate_html_layout(layed_out_interface, args.output)


if __name__ == '__main__':
    main()

