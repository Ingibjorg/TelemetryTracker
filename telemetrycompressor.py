from math import sqrt

# Input:
# ['click', 'x', 'y', 'overA', 'overB', 'overC', 'overD'])
# [0, 839, 559, 0, 0, 0, 0, 1487871142592],

# Output:
# [A, total time spent on A, total mouse velocity over A, how many times did you visit A in total,
# B, total time spent on B, total mouse velocity over B, how many times did you visit B in total,
# E, total time spent on E, total mouse velocity over E, how many times did you visit E in total,
# click (5 different values for A,B,C,D,E), 
# velocity before click, 
# how many times did you visit a button in total,
# total time before they started to make a decision (like if they
# are just still in the beginning with the mouse and then start
# to move) ]

def compress_event(events):
    """Compress event"""
    result = []
    last_ts = ""
    last_ts_a = 0
    last_ts_b = 0
    last_ts_c = 0
    last_ts_d = 0
    last_ts_e = 0
    last_x = 0
    last_y = 0

    # Values in output array:
    A = 0 # Boolean value indicating whether box was visited
    ttA = 0 # Total time spent on A (milliseconds)
    tmvA = 0
    vtA = 0 # Visit times
    B = 0; ttB = 0; tmvB = 0; vtB = 0
    C = 0; ttC = 0; tmvC = 0; vtC = 0
    D = 0; ttD = 0; tmvD = 0; vtD = 0
    E = 0; ttE = 0; tmvE = 0; vtE = 0 # E is for the area outside of the response boxes
    click = 83 # 83 for S as in silence
    vbc = 0 # Velocity before click (just before?)
    tbv = 0 # Total button visits
    ttbd = 0 # Total time before decision process

    for mouse_event in events:
        if mouse_event[3] == 1: #A
            A = 1
            current_time = mouse_event[7]
            if last_ts == "A":
                delta_time = current_time - last_ts_a
                ttA = ttA + delta_time
                distance = get_mouse_distance(last_x, mouse_event[1], last_y, mouse_event[2])
                if ttbd == 0 and distance < 5:
                    ttbd = current_time - FIRST_TS
                tmvA = tmvA + get_mouse_velocity(distance, delta_time)
            else:
                vtA = vtA + 1
                last_ts = "A"
            last_x = mouse_event[1]
            last_y = mouse_event[2]
            last_ts_a = current_time
            if mouse_event[0]:
                click = 65
        elif mouse_event[4] == 1: #B
            B = 1
            current_time = mouse_event[7]
            if last_ts == "B":
                delta_time = current_time - last_ts_b
                ttB = ttB + delta_time
                distance = get_mouse_distance(last_x, mouse_event[1], last_y, mouse_event[2])
                if ttbd == 0 and distance < 5:
                    ttbd = current_time - FIRST_TS
                tmvB = tmvB + get_mouse_velocity(distance, delta_time)
            else:
                vtB = vtB + 1
                last_ts = "B"
            last_x = mouse_event[1]
            last_y = mouse_event[2]
            last_ts_b = current_time
            if mouse_event[0]:
                click = 66
        elif mouse_event[5] == 1: #C
            C = 1
            current_time = mouse_event[7]
            if last_ts == "C":
                delta_time = current_time - last_ts_c
                ttC = ttC + delta_time
                distance = get_mouse_distance(last_x, mouse_event[1], last_y, mouse_event[2])
                if ttbd == 0 and distance < 5:
                    ttbd = current_time - FIRST_TS
                tmvC = tmvC + get_mouse_velocity(distance, delta_time)
            else:
                vtC = vtC + 1
                last_ts = "C"
            last_x = mouse_event[1]
            last_y = mouse_event[2]
            last_ts_c = current_time
            if mouse_event[0]:
                click = 67
        elif mouse_event[6] == 1: #D
            D = 1
            current_time = mouse_event[7]
            if last_ts == "D":
                delta_time = current_time - last_ts_d
                ttD = ttD + delta_time
                distance = get_mouse_distance(last_x, mouse_event[1], last_y, mouse_event[2])
                if ttbd == 0 and distance < 5:
                    ttbd = current_time - FIRST_TS
                tmvD = tmvD + get_mouse_velocity(distance, delta_time)
            else:
                vtD = vtD + 1
                last_ts = "D"
            last_x = mouse_event[1]
            last_y = mouse_event[2]
            last_ts_d = current_time
            if mouse_event[0]:
                click = 68
        else:
            E = 1 # Not over any response box
            current_time = mouse_event[7]
            if last_ts == "E":
                delta_time = current_time - last_ts_e
                ttE = current_time - last_ts_e
                distance = get_mouse_distance(last_x, mouse_event[1], last_y, mouse_event[2])
                if ttbd == 0 and distance < 5:
                    ttbd = current_time - FIRST_TS
                tmvE = tmvE + get_mouse_velocity(distance, delta_time)
            else:
                vtE = vtE + 1
                last_ts = "E"
            last_x = mouse_event[1]
            last_y = mouse_event[2]
            last_ts_e = current_time
    vbc = tmvA + tmvB + tmvC + tmvD + tmvE
    tbv = vtA + vtB + vtC + vtD + vtE
    result = [A, ttA, int(round(tmvA)), vtA, B, ttB, int(round(tmvB)), vtB,
              C, ttC, int(round(tmvC)), vtC, D, ttD, int(round(tmvD)), vtD,
              E, ttE, int(round(tmvE)), vtE, click, int(round(vbc)), tbv, ttbd]
    write_event_to_file(result)

def write_event_to_file(event):
    target = open(OUTPUT_FILE, 'a')
    target.write(str(event) + '\n')
    target.close()

def get_mouse_distance(last_x, current_x, last_y, current_y):
    delta_x = last_x - current_x
    delta_y = last_y - current_y
    return sqrt(delta_x**2 + delta_y**2)

def get_mouse_velocity(distance, time):
    if time == 0:
        return 0
    return round(distance/time, 2)

if __name__ == '__main__':
    INPUT_FILE = "./data/7/25022017-144851/00_dump_mouse_mined.txt" # raw_input("Enter file name: ")
    OUTPUT_FILE = INPUT_FILE.replace('.txt', '_compressed.txt')
    #text_file = "./data/3/23022017-171351/00_dump_mouse_mined.txt"
    INPUT_ARRAY = []

    with open(INPUT_FILE, "r") as ins:
        for line in ins:
            INPUT_ARRAY.append(eval(line))
    for events in INPUT_ARRAY:
        if events:
            FIRST_TS = events[0][7]
            compress_event(events)
        else:
            write_event_to_file([])
        