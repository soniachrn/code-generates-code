# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import layout_generator.generate_html_layout as gen
import config_reader.config_reader as cr
import autolayout.autolayout as al



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    layout = cr.read_layout_config("example.txt")
    al.autolayout(layout)
    gen.generate_html_layout(layout, "out.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
