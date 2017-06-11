import csv
import sys
import buttonlocator

def write_events_to_file(events):
    """Write mined dialogue events to a file"""
    target = open(OUTPUT_FILE, 'a')
    target.write(str(events))
    target.write('\n')
    target.close()

def get_mouse_event(click, x, y, ts):
    """Return mouse event as ['click', 'x', 'y', 'overA', 'overB', 'overC', 'overD'])"""
    overA = 0
    overB = 0
    overC = 0
    overD = 0
    if dialogue_counter == 10 or dialogue_counter == 21 or dialogue_counter == 25:
        if buttonlocator.is_left_dialogue_button(x, y):
            overA = 1
        elif buttonlocator.is_right_dialogue_button(x, y):
            overB = 1
    elif buttonlocator.is_top_left_dialogue_button(x, y):
        overA = 1
    elif buttonlocator.is_bottom_left_dialogue_button(x, y):
        overC = 1
    elif buttonlocator.is_top_right_dialogue_button(x, y):
        overB = 1
    elif buttonlocator.is_bottom_right_dialogue_button(x, y):
        overD = 1
    return [click, x, y, overA, overB, overC, overD, ts]

if __name__ == '__main__':
    INPUT_CSV = raw_input("Enter csv file name: ")
    DECISION_CSV = INPUT_CSV.replace('.csv', '_decisions.csv')
    DIALOGUE_TIMES = []
    OUTPUT_FILE = INPUT_CSV.replace('.csv', '_mined.txt')
    dialogue_counter = 0
    dialogue_events = []

    with open(DECISION_CSV, 'rb') as decision_csvfile:
        DECISION_READER = csv.reader(decision_csvfile, delimiter=';', quotechar='|')
        for row in DECISION_READER:
            DIALOGUE_TIMES.append(int(row[2]))

    with open(INPUT_CSV, 'rb') as csvfile:
        READER = csv.reader(csvfile, delimiter=';', quotechar='|')
        if 'mouse' in INPUT_CSV:
            for row in READER: # Row format: event_type;pos_x;pos_y;time
                ts = 0
                if dialogue_counter > 27:
                    sys.exit(0)
                if 'mouse_move' in row[0] or 'mouse_down_left' in row[0]:
                    x = int(row[1])
                    y = int(row[2])
                    ts = int(row[3])
                    if ts > DIALOGUE_TIMES[dialogue_counter]:
                        dialogue_counter = dialogue_counter + 1
                        write_events_to_file(dialogue_events)
                    if ts >= DIALOGUE_TIMES[dialogue_counter] - 5000 and ts < DIALOGUE_TIMES[dialogue_counter]:
                        event = get_mouse_event(0, x, y, ts)
                        dialogue_events.append(event)
                    elif ts == DIALOGUE_TIMES[dialogue_counter]:
                        click = 0
                        if 'mouse_down_left' in row[0]:
                            click = 1
                        event = get_mouse_event(click, x, y, ts)
                        dialogue_events.append(event)
                        dialogue_counter = dialogue_counter + 1
                        write_events_to_file(dialogue_events)
                        dialogue_events = []
