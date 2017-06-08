# Input:
# ['click', 'x', 'y', 'overA', 'overB', 'overC', 'overD'])
# [0, 839, 559, 0, 0, 0, 0, 1487871142592],

# Output:
# [A, total time spent on A, total mouse pace over A, how many times did you visit A in total,
# B, total time spent on B, total mouse pace over B, how many times did you visit B in total,
# E, total time spent on E, total mouse pace over E, how many times did you visit E in total,
# click (5 different values for A,B,C,D,E), 
# velocity before click (), 
# how many times did you visit a button in total,
# total time before they started to make a decision (like if they
# are just still in the beginning with the mouse and then start
# to move) ]

if __name__ == '__main__':
    INPUT_FILE = raw_input("Enter file name: ")
    OUTPUT_FILE = INPUT_FILE.replace('.txt', '_compressed.txt')
    #text_file = "./data/3/23022017-171351/00_dump_mouse_mined.txt"
    INPUT_ARRAY = []

    with open(INPUT_FILE, "r") as ins:
      for line in ins:
          INPUT_ARRAY.append(eval(line))

def compress_event(event):
    """Compress event"""
    RESULT = []
    LAST_TS = ""
    LAST_TS_A = 0
    LAST_TS_B = 0
    LAST_TS_C = 0
    LAST_TS_D = 0
    LAST_TS_E = 0

    # Values in output array:
    A = 0 # Boolean value indicating whether box was visited
    ttA = 0 # Total time spent on A (milliseconds)
    tmpA = 0
    vtA = 0
    B = 0; ttB = 0; tmpB = 0; vtB = 0; C = 0; ttC = 0; tmpC = 0; vtC = 0; D = 0; ttD = 0; tmpD = 0; vtD = 0
    E = 0; ttE = 0; tmpE = 0; vtE = 0 # E is for the area outside of the response boxes
    CLICK = 83 # 83 for S as in silence

    for mouse_event in event:
        if mouse_event[3] == 1: #A
            A = 1
            vtA = vtA + 1
            if LAST_TS == "A":
                ttA = ttA + (int(mouse_event[7]) - LAST_TS_A)
            LAST_TS_A = int(mouse_event[7])
            LAST_TS = "A"
            if mouse_event[0]:
                CLICK = 65
        elif mouse_event[4] == 1: #B
            B = 1
            vtB = vtB + 1
            if LAST_TS == "B":
                ttB = ttB + (int(mouse_event[7]) - LAST_TS_B)
            LAST_TS_B = int(mouse_event[7])
            LAST_TS = "B"
            if mouse_event[0]:
                CLICK = 66
        elif mouse_event[5] == 1: #C
            C = 1
            vtC = vtC + 1
            if LAST_TS == "C":
                ttC = ttC + (int(mouse_event[7]) - LAST_TS_C)
            LAST_TS_C = int(mouse_event[7])
            LAST_TS = "C"
            if mouse_event[0]:
                CLICK = 67
        elif mouse_event[6] == 1: #D
            D = 1
            vtD = vtD + 1
            if LAST_TS == "D":
                ttD = ttD + (int(mouse_event[7]) - LAST_TS_D)
            LAST_TS_D = int(mouse_event[7])
            LAST_TS = "D"
            if mouse_event[0]:
                CLICK = 68
        else:
            E = 1 # Not over any response box
            vtE = vtE + 1
            if LAST_TS == "E":
                ttE = int(mouse_event[7]) - LAST_TS_E
            LAST_TS_E = int(mouse_event[7])
            LAST_TS = "E"
    RESULT = [A, ttA, tmpA, vtA, B, ttB, tmpB, vtB, C, ttC, tmpC, vtC, D, ttD, tmpD, vtD,
              E, ttE, tmpE, vtE, CLICK]
    write_event_to_file(RESULT)

def write_event_to_file(event):
    target = open(OUTPUT_FILE, 'a')
    target.write(str(event) + '\n')
    target.close()


if __name__ == '__main__':
    for event in INPUT_ARRAY:
        compress_event(event)
