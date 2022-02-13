# from threading import Thread
import time
seconds = 0


def seconds_counter():
    global seconds
    while True:
        seconds += 1
        time.sleep(0.1)
        print(seconds)


seconds_counter()
