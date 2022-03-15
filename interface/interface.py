from enum import Enum


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


class Coordination:
    def __init__(self, top, left):
        self.top = top
        self.left = left


class Node:
    def __init__(self, yaml_node):
        self.width = yaml_node.get('width', None)
        self.height = yaml_node.get('height', None)
        self.position = self._get_position(yaml_node.get('position', None))
        self.color = self._get_color(yaml_node.get('color', None))
        self.coordination = Coordination(0,0)

    def _get_color(self, color):
        return color if color else 'black'

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
            return None


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
            print('Invalid interface config node {key}')
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
        self.text = yaml_node.get('text', 'Good text:))')
        super().__init__(yaml_node)


class TextField(Node):
    def __init__(self, yaml_node):
        self.text = yaml_node.get('placeholder', None)
        super().__init__(yaml_node)

