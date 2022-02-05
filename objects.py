from enum import Enum


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.red = r
        self.green = g
        self.blue = b


class Position(Enum):
    Top = 1
    Bottom = 2
    Upper = 3
    Lower = 4
    Left = 5
    Right = 6


class Textfield:
    def __init__(self):
        self.placeholder = None

        # optional sub-element
        self.label = None


class Label:
    def __init__(self):
        self.text = None


class Button:
    def __init__(self):
        self.text = None
        self.size = None
        self.color = None

        # optional sub-element
        self.label = None


class Group:
    def __init__(self):
        self.position = None
        self.name = None

        # sub-elements
        self.label = None
        self.group = None
        self.text = None
        self.button = None
        self.textfield = None


class Interface:
    def __init__(self):
        self.text = None
        self.size = None
        self.name = None

        # sub-elements
        self.label = None
        self.group = None
        self.text = None
        self.button = None
        self.textfield = None
