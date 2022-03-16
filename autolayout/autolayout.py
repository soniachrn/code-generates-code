
# Fill layout coordinates etc.
from interface.interface import *

DOWN_SHIFT_PERCENTAGE = 3
OBJ_EXPENSES = 4
TEXTFIELD_BORDER = 3

def count_shift_to_the_right(layout):
    cnt = 0
    for child in layout.children:
        if type(child) == '<class \'interface.interface.Group\'>':
           cnt += count_shift_to_the_right(child)
        if child.position and child.position in [
            Position.RIGHT,
            Position.UPPER_RIGHT,
            Position.LOWER_RIGHT,
            Position.LEFT
        ]:
            if isinstance(child, Group):
                cnt += len(child.children)
            else:
                cnt += 1
        else:
            if isinstance(child, Group):
                cnt += count_shift_to_the_right(child)
    return cnt

def layout_node(layout, top, left, shift, height):
    for child in layout.children:
        if isinstance(child, Group):
            group_left = 0
            group_top = 0
            if child.position:
                if child.position == Position.RIGHT:
                    group_left += shift
                if child.position == Position.LEFT:
                    group_left -= shift
                if child.position == Position.TOP:
                    group_top -= DOWN_SHIFT_PERCENTAGE
                if child.position == Position.BOTTOM:
                    group_top += DOWN_SHIFT_PERCENTAGE
                if child.position == Position.CENTER:
                    group_left += shift / 2 - shift / 4 # approximately in the center of block. TODO: recognize group center
                if child.position == Position.UPPER_RIGHT: # 45 degrees rotation
                    group_top -= 3 * DOWN_SHIFT_PERCENTAGE / 2
                    group_left += shift / 2
                if child.position == Position.UPPER_LEFT:
                    group_top -= 3 * DOWN_SHIFT_PERCENTAGE / 2
                    group_left -= shift / 2
                if child.position == Position.LOWER_LEFT:
                    group_top += 3 * DOWN_SHIFT_PERCENTAGE / 2
                    group_left -= shift / 2
                if child.position == Position.LOWER_RIGHT:
                    group_top += 3 * DOWN_SHIFT_PERCENTAGE / 2
                    group_left += shift / 2
            else:
                group_top += DOWN_SHIFT_PERCENTAGE
            curr_top = layout_node(child, top + group_top, left + group_left, shift, height)
            top += group_top + top - curr_top
            if child.position and child.position == Position.TOP:
                top += 2 * DOWN_SHIFT_PERCENTAGE
        else:
            if isinstance(child, TextField) or isinstance(child, Button): #border around
                top += TEXTFIELD_BORDER
            print('Top ' + str(top))

            if child.position:
                if child.position == Position.RIGHT:
                    child.coordination.left = left + shift
                    child.coordination.top = top
                if child.position == Position.LEFT:
                    print('Left')
                    print(top)
                    child.coordination.left = left - shift
                    child.coordination.top = top
                if child.position == Position.TOP:
                    child.coordination.top = top - DOWN_SHIFT_PERCENTAGE
                    child.coordination.left = left
                if child.position == Position.BOTTOM:
                    child.coordination.top = top + DOWN_SHIFT_PERCENTAGE
                    child.coordination.left = left
                if child.position == Position.CENTER:
                    child.coordination.left = left + shift / 6
                    child.coordination.top = top
                if child.position == Position.UPPER_RIGHT:
                    child.coordination.top = top - 3 * DOWN_SHIFT_PERCENTAGE / 2
                    child.coordination.left = left + shift / 2
                if child.position == Position.UPPER_LEFT:
                    child.coordination.top = top - 3 * DOWN_SHIFT_PERCENTAGE / 2
                    child.coordination.left = left - shift / 2
                if child.position == Position.LOWER_LEFT:
                    child.coordination.top = top + 3 * DOWN_SHIFT_PERCENTAGE / 2
                    child.coordination.left = left - shift / 2
                if child.position == Position.LOWER_RIGHT:
                    child.coordination.top = top + 3 * DOWN_SHIFT_PERCENTAGE / 2
                    child.coordination.left = left + shift / 2
                if child.position == Position.NATIVE:
                    print('Native right ' + str(left))
                    child.coordination.top = top
                    child.coordination.left = left
            else:
                child.coordination.left = left
                child.coordination.top = top
            if child.height:
                top += 100 * child.height / height + OBJ_EXPENSES + 1
        if not child.position:
            top += DOWN_SHIFT_PERCENTAGE
    return top

def count_negative_coordinates(layout):
    min_top = 0
    min_left = 0
    for child in layout.children:
        if isinstance(child, Group):
            group_top, group_left = count_negative_coordinates(child)
            if group_top < min_top:
                min_top = group_top
            if group_left < min_left:
                min_left = group_left
        if child.coordination:
            if child.coordination.left < min_left:
                min_left = child.coordination.left
            if child.coordination.top < min_top:
                min_top = child.coordination.top
    return min_top, min_left

def move_each_child(layout, top, left):
    for child in layout.children:
        if isinstance(child, Group):
            move_each_child(child, top, left)
        elif child.coordination:
            child.coordination.left += left
            child.coordination.top += top

def autolayout(layout):
    right_shift = count_shift_to_the_right(layout)
    shift = 2
    if right_shift:
        part = layout.width / right_shift
        shift = 100 * part / layout.width
    print(shift)
    layout_node(layout, 0, 0, shift, layout.height)
    min_top, min_left = count_negative_coordinates(layout)
    print(min_top)
    move_each_child(layout, abs(min_top), abs(min_left))