from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pymouse import PyMouseEvent

class MouseTracker(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def move(self, x, y):
        print(x)
        print(y)


    def click(self, x, y, button, press):
        if button == 1:
            if press:
                print("SUCC")
        else:  # Exit if any other mouse button used
            self.stop()

M = MouseTracker()
M.run()
