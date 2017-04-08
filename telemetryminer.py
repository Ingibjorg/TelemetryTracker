import csv
import sys

#['click', 'x', 'y', 'overA', 'overB', 'overC', 'overD'])

# Top left dialogue button
# x: 134 - 134+807
# y: 797 - 797+84
def is_top_left_dialogue_button(pos_x, pos_y):
    """Return true if position is within the top left dialogue button"""
    if pos_x >= 134 and pos_x <= (134+807) and pos_y >= 797 and pos_y <= (797+84):
        return True

# Bottom left dialogue button
# x: 134 - 134+807
# y: 900 - 900+84
def is_bottom_left_dialogue_button(pos_x, pos_y):
    """Return true if position is within the bottom left dialogue button"""
    if pos_x >= 134 and pos_x <= (134+807) and pos_y >= 897 and pos_y <= (897+84):
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
# y: 900 - 900+84
def is_bottom_right_dialogue_button(pos_x, pos_y):
    """Return true if position is within the bottom right dialogue button"""
    if pos_x >= 978 and pos_x <= (978+807) and pos_y >= 897 and pos_y <= (897+84):
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
    INPUT_CSV = 'data/3/23022017-171351/00_dump_mouse.csv' #raw_input("Enter csv file name: ")
    #DIALOGUE_TIMES = raw_input("Enter start times: (Format: [1487877840000, 1487877840000...]) ")
    DECISION_CSV = INPUT_CSV.replace('.csv', '_decisions.csv')
    DIALOGUE_TIMES = []
    OUTPUT_FILE = INPUT_CSV.replace('.csv', '_mined.txt')

    with open(DECISION_CSV, 'rb') as decision_csvfile:
        DECISION_READER = csv.reader(decision_csvfile, delimiter=';', quotechar='|')
        for row in DECISION_READER:
            DIALOGUE_TIMES.append(int(row[2]))

    with open(INPUT_CSV, 'rb') as csvfile:
        READER = csv.reader(csvfile, delimiter=';', quotechar='|')
        desicions = ''
        if 'mouse' in INPUT_CSV:
            # Row format: event_type;pos_x;pos_y;time
            dialogue_counter = 0
            dialogue_events = [] # events per dialogue
            for row in READER:
                click = 0
                overA = 0
                overB = 0
                overC = 0
                overD = 0
                ts = 0
                if dialogue_counter > 27:
                    sys.exit(0)
                if 'mouse_move' in row[0] or 'mouse_down_left' in row[0]:
                    x = int(row[1])
                    y = int(row[2])
                    ts = int(row[3])
                if 'mouse_move' in row[0]:
                    # click;x;y;overA;overB;overC;overD;
                    if ts >= DIALOGUE_TIMES[dialogue_counter] - 5000 and ts <= DIALOGUE_TIMES[dialogue_counter]:
                        if dialogue_counter == 10 or dialogue_counter == 21 or dialogue_counter == 25:
                            if is_left_dialogue_button(x, y):
                                overA = 1
                            elif is_right_dialogue_button(x, y):
                                overB = 1
                        elif is_top_left_dialogue_button(x, y):
                            overA = 1
                        elif is_bottom_left_dialogue_button(x, y):
                            overC = 1
                        elif is_top_right_dialogue_button(x, y):
                            overB = 1
                        elif is_bottom_right_dialogue_button(x, y):
                            overD = 1
                        event = [click, x, y, overA, overB, overC, overD, row[3]]
                        dialogue_events.append(event)
                if ts == DIALOGUE_TIMES[dialogue_counter]:
                    print row
                    # TODO Treat silences
                    click = 1
                    if dialogue_counter == 10 or dialogue_counter == 21 or dialogue_counter == 25:
                        if is_left_dialogue_button(x, y):
                            overA = 1
                        elif is_right_dialogue_button(x, y):
                            overB = 1
                    elif is_top_left_dialogue_button(x, y):
                        overA = 1
                    elif is_bottom_left_dialogue_button(x, y):
                        overC = 1
                    elif is_top_right_dialogue_button(x, y):
                        overB = 1
                    elif is_bottom_right_dialogue_button(x, y):
                        overD = 1
                    event = [click, x, y, overA, overB, overC, overD, row[3]]
                    dialogue_events.append(event)
                    dialogue_counter = dialogue_counter + 1
                    target = open(OUTPUT_FILE, 'a')
                    target.write('Dialogue ' + str(dialogue_counter) + ' events: ' + len(dialogue_events) + '\n')
                    target.write(str(dialogue_events))
                    target.write('\n')
                    target.close()
                    dialogue_events = []
