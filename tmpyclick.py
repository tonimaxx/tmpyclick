# from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from pynput.mouse import Listener as MouseListener
from pynput import keyboard
from queue import Queue

# keyboard = KeyboardController()
mouse = MouseController()


# Mouse Handler
def on_click(x, y, button, pressed):
    if pressed:
        # print('Pressed {0}'.format(button))
        print(button)
        if button == Button.middle:
            # print("Hello middle")
            mouse.click(Button.left, 120)

with MouseListener(on_click=on_click) as mouselistener:
    mouselistener.join()




# mouse.move(20, 500)
# mouse.click(Button.right, 20)