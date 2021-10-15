from pynput import keyboard
from queue import Queue

message = ''
keys = []

queue = Queue()

def write_keys(keys):
    global message
    for key in keys:
        k = str(key).replace(f'{chr(39)}', '')
        print(k)
        message += k
    if len(message) == 10:
        queue.put(message)

def on_press(key):
    global keys
    keys.append(key)
    write_keys(keys)
    keys = []

keyboard_thread = keyboard.Listener(on_press=on_press)
keyboard_thread.start()
while True:
    messages = queue.get()
    print(messages)