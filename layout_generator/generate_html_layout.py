
# Generate an html file by the given layout

class HTMLGenerator:
    def __init__(self):
        self.styles = []
        self.bodies = []
        self.buttons = 0
        self.labels = 0
        self.text_fields = 0

    def generate(self, layout):
        for child in layout.children:
            node_type = type(child)
            if node_type == 'Button':
                self._generate_button(child)
            elif node_type == 'Label':
                self._generate_label(child)
            elif node_type == 'TextField':
                self._generate_textfield(child)


    def _generate_button(self, button):
        self.buttons += 1
        style = '''
        .button{button_no} {
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
        }'''.format(button_no=self.buttons,
                    bg_color=button.bg_color,
                    text_color=button.text_color,
                    top=button.position.top,
                    left=button.position.left)

        body = '<button class="button{button_no}">{text}</button>'.format(button_no=self.buttons, text=button.text)
        self.styles.append(style)
        self.bodies.append(body)

    def _generate_label(self, label):
        self.labels += 1
        style = '''
        .label{label_no} {
            position:absolute;
            top: {top}%;
            left: {left}%;
        }'''.format(label_no=self.labels,
                    top=label.position.top,
                    left=label.position.left)

        body = '<p class="label{label_no}">{text}</p>'.format(label_no=self.buttons, text=label.text)
        self.styles.append(style)
        self.bodies.append(body)

    def _generate_textfield(self, textfield):
        self.text_fields += 1
        style = '''
                .textfield{textfield_no} {
                    border: 3px groove #FFFFFF;
                    outline:0;
                    height:{height}px;
                    width: {width}px;
                    position:absolute;
                    top: {top}%;
                    left: {left}%;
                }'''.format(textfield_no=self.text_fields,
                            height=label.height,
                            width=label.width,
                            top=label.position.top,
                            left=label.position.left)

        body = '<input class="textfield{textfield_no}" type="text">'.format(textfield_no=self.text_fields)
        self.styles.append(style)
        self.bodies.append(body)

    def print_styles(self):
        for style in self.styles:
            print(style)

    def print_bodies(self):
        for body in self.bodies:
            print(body)


def generate_html_layout(layout, output_file_path: str):
    generator = HTMLGenerator()
    generator.generate(layout)
    print('''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
    ''')

    generator.print_styles()

    print('''
        </style>
        </head>
        <body>
    ''')

    generator.print_bodies()

    print('''
        </body>
        </html>
    ''')
