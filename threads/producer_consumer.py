import logging
import random
import threading

SENTINEL = object()


def producer(pipeline):
    """Pretend we are getting a message from the network"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel a message to tell consumer we are done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """Pretend we are saving a number in the database"""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


class Pipeline:
    """Class to allow a single element pipeline between producer and consumer"""

    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s: about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s: have getlock", name)
        message = self.message
        logging.debug("%s: about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s: setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s: about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s: have setlock", name)
        self.message = message
        logging.debug("%s: about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s: getlock release", name)