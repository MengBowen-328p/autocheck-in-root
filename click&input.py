from pykeyboard import PyKeyboard
from pymouse import PyMouse

def click(x,y):
    m = PyMouse()
    print(m.position())
    m.move(x,y)
    m.click()
    print("clicked")

def input(inputString):
    k = PyKeyboard()
    print("The string will be typed is"+inputString)
    k.type_string(inputString)
    print("typed")
