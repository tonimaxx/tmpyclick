from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key
import logging

mouse = MouseController()

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def end_rec(key):
    pass
    # logging.info(str(key))

def on_press(key):
    print(f"Hello {str(key)}")
    if str(key) == "'g'":
        mouse.click(Button.left, 20)
        # print("Hello cccccc")
    if key == Key.esc:
        exit()

    # logging.info(str(key))

def on_move(x, y):
    pass
    # logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print(button)
        # logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        if button == Button.middle:
            # print("Hello middle")
            mouse.click(Button.left, 20)

def on_scroll(x, y, dx, dy):
    # logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    pass


with MouseListener(on_click=on_click, on_scroll=on_scroll) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()