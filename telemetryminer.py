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

def write_events_to_file(events):
    target = open(OUTPUT_FILE, 'a')
    target.write('Dialogue ' + str(dialogue_counter) + ' events: ' + str(len(events)) + '\n')
    target.write(str(events))
    target.write('\n')
    target.close()

def get_mouse_event(click, x, y, ts):
    overA = 0
    overB = 0
    overC = 0
    overD = 0
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
    return [click, x, y, overA, overB, overC, overD, ts]

if __name__ == '__main__':
    INPUT_CSV = raw_input("Enter csv file name: ")
    DECISION_CSV = INPUT_CSV.replace('.csv', '_decisions.csv')
    DIALOGUE_TIMES = []
    SILENCE_TIMES = []
    OUTPUT_FILE = INPUT_CSV.replace('.csv', '_mined.txt')
    dialogue_counter = 0
    dialogue_events = [] # events per dialogue

    with open(DECISION_CSV, 'rb') as decision_csvfile:
        DECISION_READER = csv.reader(decision_csvfile, delimiter=';', quotechar='|')
        for row in DECISION_READER:
            if 'Silence' in row[1]:
                SILENCE_TIMES.append(int(row[2]))
            DIALOGUE_TIMES.append(int(row[2]))

    with open(INPUT_CSV, 'rb') as csvfile:
        READER = csv.reader(csvfile, delimiter=';', quotechar='|')
        if 'mouse' in INPUT_CSV:
            # Row format: event_type;pos_x;pos_y;time
            for row in READER:
                ts = 0
                if dialogue_counter > 27:
                    sys.exit(0)
                if 'mouse_move' in row[0] or 'mouse_down_left' in row[0]:
                    x = int(row[1])
                    y = int(row[2])
                    ts = int(row[3])
                if 'mouse_move' in row[0]:
                    if ts >= DIALOGUE_TIMES[dialogue_counter] - 5000 and ts <= DIALOGUE_TIMES[dialogue_counter]:
                        event = get_mouse_event(0, x, y, ts)
                        dialogue_events.append(event)
                    elif ts >= DIALOGUE_TIMES[dialogue_counter]:
                        for silence in SILENCE_TIMES:
                            if DIALOGUE_TIMES[dialogue_counter] == int(silence):
                                dialogue_events.append(event)
                                dialogue_counter = dialogue_counter + 1
                                write_events_to_file(dialogue_events)
                                dialogue_events = []
                if ts == DIALOGUE_TIMES[dialogue_counter]:
                    click = 0
                    if 'mouse_down_left' in row[0]:
                        click = 1
                    event = get_mouse_event(1, x, y, ts)
                    dialogue_events.append(event)
                    dialogue_counter = dialogue_counter + 1
                    write_events_to_file(dialogue_events)
                    dialogue_events = []
