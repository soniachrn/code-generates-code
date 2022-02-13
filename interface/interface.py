from enum import Enum
import lorem


DEFAULT_IMAGE_URL = 'https://artprojectsforkids.org/wp-content/uploads/2020/08/Elephant-recolor.jpg'


class Position(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4
    UPPER_LEFT = 5
    UPPER_RIGHT = 6
    LOWER_LEFT = 7
    LOWER_RIGHT = 8
    CENTER = 9


class Node:
    def __init__(self, yaml_node):
        self.width = yaml_node.get('width', None)
        self.height = yaml_node.get('height', None)
        self.position = self._get_position(yaml_node.get('position', None))

    def _get_position(self, position_str):
        positions = {
            None: None,
            'top': Position.TOP,
            'bottom': Position.BOTTOM,
            'left': Position.LEFT,
            'right': Position.RIGHT,
            'upper left': Position.UPPER_LEFT,
            'upper right': Position.UPPER_RIGHT,
            'lower left': Position.LOWER_LEFT,
            'lower right': Position.LOWER_RIGHT,
            'center': Position.CENTER,
        }

        if position_str in positions:
            return positions[position_str]
        else:
            print(f'Invalid node position {position_str}')
            exit(1)


class Button(Node):
    def __init__(self, yaml_node):
        self.text = yaml_node.get('text', 'Button')
        super().__init__(yaml_node)


class Group(Node):
    def __init__(self, yaml_node):
        self.children = [self._read_child(child) for child in yaml_node.get('children', [])]
        super().__init__(yaml_node)

    def _read_child(self, child):
        if type(child) is dict:
            assert(len(child) == 1)
            key, value = list(child.items())[0]
        else:
            assert(type(child) is str)
            key, value = child, dict()

        if key == 'button':
            return Button(value)
        elif key == 'group':
            return Group(value)
        elif key == 'image':
            return Image(value)
        elif key == 'label':
            return Label(value)
        elif key == 'text':
            return Text(value)
        elif key == 'textfield':
            return TextField(value)
        else:
            print(f'Invalid interface config node {key}')
            exit(1)


class Image(Node):
    def __init__(self, yaml_node):
        self.url = yaml_node.get('url', DEFAULT_IMAGE_URL)
        super().__init__(yaml_node)


class Interface(Group):
    def __init__(self, yaml_node):
        super().__init__(yaml_node)


class Label(Node):
    def __init__(self, yaml_node):
        self.text = yaml_node.get('text', 'Label')
        super().__init__(yaml_node)


class Text(Node):
    def __init__(self, yaml_node):
        self.text = yaml_node.get('text', lorem.text())
        super().__init__(yaml_node)


class TextField(Node):
    def __init__(self, yaml_node):
        self.text = yaml_node.get('placeholder', None)
        super().__init__(yaml_node)
