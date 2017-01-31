import datetime
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pymouse import PyMouseEvent

class MouseTracker(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def move(self, x, y):
        position = (x, y)
        mousePosition = 'X: {0[0]},  Y: {0[1]}\n'.format(position)
        logTelemetry(mousePosition)
        print(('X: {0[0]},  Y: {0[1]}').format(position))

    def click(self, x, y, button, press):
        # TODO Track mouse click

def logTelemetry(log):
    f = open(logFileName, 'a+')
    f.write(log)

# Configure log filename
d = datetime.date.today()
logFileName = d.strftime('Logs/WAU_%d_%m_%Y_%H_%M_%S.txt')

M = MouseTracker()
M.run()
