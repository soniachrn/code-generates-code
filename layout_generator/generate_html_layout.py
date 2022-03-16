# Generate an html file by the given layout
from interface.interface import *
from autolayout.autolayout import OBJ_EXPENSES

class HTMLGenerator:
    def __init__(self):
        self.styles = []
        self.bodies = []
        self.buttons = 0
        self.labels = 0
        self.text_fields = 0
        self.images = 0

    def generate(self, layout):
        for child in layout.children:
            node_type = str(type(child))
            print(node_type)
            if node_type == '<class \'interface.interface.Button\'>':
                self._generate_button(child)
            elif node_type == '<class \'interface.interface.Label\'>' or node_type == '<class \'interface.interface.Text\'>':
                print('Here')
                self._generate_label(child)
            elif node_type == '<class \'interface.interface.TextField\'>':
                self._generate_textfield(child)
            elif node_type == '<class \'interface.interface.Image\'>':
                self._generate_image(child)
            elif node_type == '<class \'interface.interface.Group\'>':
                self.generate(child)

    def _generate_image(self, image):
        self.images += 1
        style = '''
        .image{image_no} {{
            position:absolute;
            top: {top}%;
            left: {left}%;
        }}'''.format(image_no=self.images, top=image.coordination.top + OBJ_EXPENSES,
                    left=image.coordination.left)
        
        body = '<img class="image{image_no}" src=\"{img}\" width=\"{w}\" height=\"{h}\">'.format(image_no=self.images, img=image.url, w=image.width, h=image.height)
        self.bodies.append(body)
        self.styles.append(style)

    def _generate_button(self, button):
        self.buttons += 1
        print('In button')
        style = '''
        .button{button_no} {{
            background-color: {bg_color};
            border: none;
            color: {text_color};
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            position:absolute;
            top: {top}%;
            left: {left}%;
        }}'''.format(button_no=self.buttons,
                    bg_color=button.color,
                    text_color=button.text_color,
                    top=button.coordination.top,
                    left=button.coordination.left)

        print('In button2')
        body = '<button class="button{button_no}">{text}</button>'.format(button_no=self.buttons, text=button.text)
        self.styles.append(style)
        self.bodies.append(body)

    def _generate_label(self, label):
        self.labels += 1
        style = '''
        .label{label_no} {{
            color: {color};
            position: absolute;
            top: {top}%;
            left: {left}%;
        }}'''.format(label_no=self.labels,
                     color=label.color,
                     top=label.coordination.top,
                     left=label.coordination.left)

        body = '<p class="label{label_no}">{text}</p>'.format(label_no=self.labels, text=label.text)
        self.styles.append(style)
        self.bodies.append(body)

    def _generate_textfield(self, textfield):
        self.text_fields += 1
        style = '''
                .textfield{textfield_no} {{
                    border: 3px groove #FFFFFF;
                    outline:0;
                    height:{height}px;
                    width: {width}px;
                    position:absolute;
                    top: {top}%;
                    left: {left}%;
                }}'''.format(textfield_no=self.text_fields,
                            height=textfield.height,
                            width=textfield.width,
                            top=textfield.coordination.top,
                            left=textfield.coordination.left)

        body = '<input class="textfield{textfield_no}" type="text">'.format(textfield_no=self.text_fields)
        self.styles.append(style)
        self.bodies.append(body)

    def print_styles(self, out):
        for style in self.styles:
            out.write(style)

    def print_bodies(self, out):
        for body in self.bodies:
            out.write(body)
            out.write('\n')


def generate_html_layout(layout, output_file_path):
    out = open(output_file_path, 'w')

    generator = HTMLGenerator()
    generator.generate(layout)
    out.write('''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
    ''')

    generator.print_styles(out)

    out.write('''
        </style>
        </head>
        <body>
    ''')

    generator.print_bodies(out)

    out.write('''
        </body>
        </html>
    ''')