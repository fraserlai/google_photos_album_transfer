import os
from time import sleep

def upload_images(images_queue):
    while True:
        if not images_queue.empty():
            sleep(1)
            os.remove(images_queue.get())