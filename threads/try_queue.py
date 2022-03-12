import logging
import queue as q
import random


def producer(pipeline, event):

    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exciting")


def consumer(pipeline, event):

    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s (queue size=%d)",
            message,
            pipeline.qsize(),
        )
    logging.info("Consumer received EXIT event. Exciting")


class Pipeline(q.Queue):
    def __init__(self):
        super(Pipeline, self).__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("%s: about to get from queue", name)
        value = self.get()
        logging.debug("%s: got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s: about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s: added %d to queue", name, value)
