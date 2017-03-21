import csv

# Top left dialogue button
# x: 134 - 134+807
# y: 797 - 797+84
def is_top_left_dialogue_button(pos_x, pos_y):
    """Return true if position is within the top left dialogue button"""
    if pos_x >= 134 and pos_x <= (134+807) and pos_y >= 797 and pos_y <= (797+84):
        return True

# Bottom left dialogue button
# x: 134 - 134+807
# y: 983 - 983+84
def is_bottom_left_dialogue_button(pos_x, pos_y):
    """Return true if position is within the bottom left dialogue button"""
    if pos_x >= 134 and pos_x <= (134+807) and pos_y >= 983 and pos_y <= (983+84):
        return True

# Top right dialogue button
# x: 978 - 978+807
# y: 797 - 797+84
def is_top_right_dialogue_button(pos_x, pos_y):
    """Return true if position is within the top right dialogue button"""
    if pos_x >= 978 and pos_x <= (978+807) and pos_y >= 797 and pos_y <= (797+84):
        return True

# Bottom right dialogue button
# x: 978 - 978+807
# y: 983 - 983+84
def is_bottom_right_dialogue_button(pos_x, pos_y):
    """Return true if position is within the bottom right dialogue button"""
    if pos_x >= 978 and pos_x <= (978+807) and pos_y >= 983 and pos_y <= (983+84):
        return True

# Left dialogue button (when they're only two)
# x: 136 - 136+807
# y: 847 - 847+84
def is_left_dialogue_button(pos_x, pos_y):
    """Return true if position is within the left dialogue button"""
    if pos_x >= 136 and pos_x <= (136+807) and pos_y >= 847 and pos_y <= (847+84):
        return True

# Right dialogue button (when they're only two)
# x: 978 - 978+807
# y: 847 - 847+84
def is_right_dialogue_button(pos_x, pos_y):
    """Return true if position is within the right dialogue button"""
    if pos_x >= 978 and pos_x <= (978+807) and pos_y >= 847 and pos_y <= (847+84):
        return True


if __name__ == '__main__':
    INPUT_CSV = raw_input("Enter csv file name: ")

    with open(INPUT_CSV, 'rb') as csvfile:
        READER = csv.reader(csvfile, delimiter=';', quotechar='|')
        if 'mouse' in INPUT_CSV:
            for row in READER:
                if 'mouse_down_left' in row[0]:
                    print row
                    x = int(row[1])
                    y = int(row[2])
                    if is_top_left_dialogue_button(x, y):
                        print 'top left'
                    elif is_bottom_left_dialogue_button(x, y):
                        print 'bottom left'
                    elif is_top_right_dialogue_button(x, y):
                        print 'top right'
                    elif is_bottom_right_dialogue_button(x, y):
                        print 'bottom right'
                    elif is_left_dialogue_button(x, y):
                        print 'left'
                    elif is_bottom_right_dialogue_button(x, y):
                        print 'right'
