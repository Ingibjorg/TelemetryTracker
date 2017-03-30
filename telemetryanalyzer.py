from collections import namedtuple
import csv
import sys

FilteredEvent = namedtuple('FilteredEvent', ['event_type', 'pos_x', 'pos_y', 'time'])
DecisionEvent = namedtuple('DecisionEvent', ['event_type', 'decision', 'time'])
DIALOGUE_ARRRAY = [
    ['I\'m looking at a 3 foot toad.', 'Enough excuses, Toad.', 'No harm done.', '...'],
    ['I don\'t make the rules.', 'Get it fixed.', 'Not my problem.', '...'],
    ['So what have I walked into?', 'What do you want me to do?', '[Head Upstairs]', '...'],
    ['Do it yourself', 'Why\'s he so pissed?', 'I\'m heading up.', '...'],
    ['What\'s going on here?', 'Alright, why\'d you hit her?', 'Everyone calm down!', '...'],
    ['This is your last warning.', 'You\'re drunk...', '[threaten him]', '...'],
    ['Say that word again.', 'SHUT UP!', 'Be nice, or I\'ll make you wait outside.', '...'],
    ['What happened?', 'What are you doing here?', 'You need to leave.', '...'],
    ['What happened?', 'You need to leave.', 'Are you alright?', '...'],
    ['What\'s your name?', 'Are you hurt?', 'Why was he hitting you?', '...'],
    ['HEY!', '[Throw him out]', 'Will you excuse me a moment?', '...'],
    ['Sorry about the car.', 'Get off the street.', 'How\'s your insurance?', '...'],
    ['What are you doing?', 'Leave him alone.', 'Thanks...', '...'],
    ['Let her', 'Stop her'],
    ['Light her cigarette...', 'Make a joke...', 'Got an extra?', '...'],
    ['Beautiful...', 'Stop changing the subject.', 'I\'m trying to help you.', '...'],
    ['This is about Fabletown.', 'He hit you.', 'Are you sure?', '...'],
    ['[give her some money]', 'Wish I could help.'],
    ['That\'s harsh.', 'I clean up okay.', 'Tell me what you really think.', '...'],
    ['Don\'t make me come over there.', 'Come on out.', 'Stay off the grass.' '...'],
    ['Out pretty late.', 'Why did you hide?', 'Where are you going?', '...'],
    ['I promise.', 'No. I can\'t do that.', 'I\'m staying out of it.', '...'],
    ['I did.', 'Haven\'t seen her.', 'Staying out of this.', '...'],
    ['Yeah. Get out.', 'There\'s only the one.', 'C\'mon, I\'m tired.', '...'],
    ['Don\'t be dramatic.', 'I won\'t.', 'Tell you what I told Toad...', '...'],
    ['I just want some rest.', '[Take a Sip]'],
    ['Everyone hates me?', 'Better to be feared...', 'I was just hungry.', '...'],
    ['My job', 'Not my fault', 'Don\'t need advice.', '...'],
    ['There was a girl...', 'Beauty', 'Toad', '...'],
    ['[Give Colin a Drink]', '[Take Drink]'],
    ['What happened?', 'Where are we going?', 'Slow down', '...'],
    ['A working girl.', 'Just a girl.', 'Prostitute.', '...']
]
DIALOGUE_DISTRIBUTION = [
    0, #0
    50,
    40,
    30,
    0,
    50, #5
    0,
    25,
    20,
    30,
    50, #10
    50,
    0,
    50,
    50,
    50, #15
    50,
    50,
    70,
    0,
    30, #20
    50,
    0,
    0,
    70,
    35, #25
    50,
    60,
    60,
    60,
    75, #30
    110]
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

def filter_csv():
    """Filter out timecodes before the actual start times"""
    with open(INPUT_CSV, 'rb') as inputcsvfile, open(FILTERED_CSV, 'wb') as filter_out:
        input_reader = csv.reader(inputcsvfile, delimiter=';', quotechar='|')
        input_writer = csv.DictWriter(filter_out, FilteredEvent._fields, delimiter=';')
        filtered_events = []

        for input_row in input_reader:
            if START_TIME < input_row[3]:
                event = FilteredEvent(input_row[0], input_row[1], input_row[2], input_row[3])
                filtered_events.append(event)
                input_writer.writerows([evt._asdict() for evt in filtered_events])
                filtered_events = []

def get_dialogue(counter, pos, decision_writer):
    """Get dialogue at certain time"""
    decision_events = []
    if len(DIALOGUE_ARRRAY) > counter:
        # Check whether we currently only have 2 dialogue options
        if dialogue_counter == 13 or dialogue_counter == 17 or dialogue_counter == 25 or dialogue_counter == 29:
            if pos == 2:
                pos = 0
            if pos == 3:
                pos = 1
        if DIALOGUE_ARRRAY[counter].count > pos:
            event = DecisionEvent('dialogue', DIALOGUE_ARRRAY[counter][pos], row[3])
            decision_events.append(event)
            decision_writer.writerows([evt._asdict() for evt in decision_events])
            print DIALOGUE_ARRRAY[counter][pos]
            return True
    return False

if __name__ == '__main__':
    INPUT_CSV = raw_input("Enter csv file name: ")
    START_TIME = raw_input("Enter start time: (Format: 1487877840000) ")
    FILTERED_CSV = INPUT_CSV.replace('.csv', '_filtered.csv')
    DECISIONS_CSV = INPUT_CSV.replace('.csv', '_decisions.csv')

    filter_csv()

    with open(FILTERED_CSV, 'rb') as csvfile, open(DECISIONS_CSV, 'wb') as out:
        READER = csv.reader(csvfile, delimiter=';', quotechar='|')
        WRITER = csv.DictWriter(out, DecisionEvent._fields, delimiter=';')
        if 'mouse' in FILTERED_CSV:
            # Row format: event_type;pos_x;pos_y;time
            dialogue_counter = 0
            last_timestamp = 0
            for row in READER:
                if 'mouse_down_left' in row[0]:
                    x = int(row[1])
                    y = int(row[2])
                    timestamp = int(row[3])
                    last_move_timestamp = 0
                    if dialogue_counter > 31:
                        sys.exit(0)
                    if DIALOGUE_DISTRIBUTION[dialogue_counter] != 0 and (timestamp - last_timestamp >= (DIALOGUE_DISTRIBUTION[dialogue_counter] * 1000)):
                        next_time = last_timestamp + (DIALOGUE_DISTRIBUTION[dialogue_counter] * 1000)
                        dialogue_counter = dialogue_counter + 1
                        print 'bump to ' + str(dialogue_counter)
                        if timestamp - next_time >= (DIALOGUE_DISTRIBUTION[dialogue_counter] * 1000):
                            dialogue_counter = dialogue_counter + 1
                            print 'bump to ' + str(dialogue_counter)
                    if (last_timestamp > 0 and timestamp - last_timestamp <= 700) or (last_move_timestamp > 0 and last_move_timestamp <= 700):
                        # Remove event - double mouse click probably 
                        print ''
                    elif is_top_left_dialogue_button(x, y):
                        #print 'top left'
                        if get_dialogue(dialogue_counter, 0, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    elif is_bottom_left_dialogue_button(x, y):
                        #print 'bottom left'
                        if get_dialogue(dialogue_counter, 2, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    elif is_top_right_dialogue_button(x, y):
                        #print 'top right'
                        if get_dialogue(dialogue_counter, 1, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    elif is_bottom_right_dialogue_button(x, y):
                        #print 'bottom right'
                        if get_dialogue(dialogue_counter, 3, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    elif is_left_dialogue_button(x, y):
                        #print 'left'
                        if get_dialogue(dialogue_counter, 0, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    elif is_bottom_right_dialogue_button(x, y):
                        #print 'right'
                        if get_dialogue(dialogue_counter, 1, WRITER):
                            dialogue_counter = dialogue_counter + 1
                            last_timestamp = timestamp
                    last_move_timestamp = timestamp
        elif 'keyboard' in FILTERED_CSV:
            # Row format: event_type;key_code;key_code_readable;scan_code;alt_pressed;time
            for row in READER:
                print row
