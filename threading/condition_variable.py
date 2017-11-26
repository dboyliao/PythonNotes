#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
from threading import Thread, Condition, Lock
import logging
import threading

logging.basicConfig(level=logging.DEBUG,
                    format="[%(threadName)-9s] %(message)s")

TASK_CAPACITY = 5
TOTAL_TASKS = 10
tasks = []

def producer(cv):
    logging.debug("producer thread start")
    while True:
        # with statement will acquire the cv
        with cv:
            if len(tasks) < 5:
                logging.debug("insert number")
                tasks.append(3)
                cv.notify()
                break
            else:
                logging.debug("waiting")
                # cv.wait will release the lock and enter a wait queue.
                # the procuder will be blocked at here and continue util
                # someone else called cv.notify
                cv.wait()
        # cv released
    logging.debug("producer exit")


def consumer(cv):
    logging.debug("consumer start")
    count = 0
    while count < TOTAL_TASKS:
        with cv:
            if tasks:
                logging.debug("consume task: {}".format(count))
                tasks.pop(0)
                count += 1
                cv.notify()
            else:
                logging.debug("waiting")
                cv.wait()
    logging.debug("consumer exit")


if __name__ == "__main__":
    cv = Condition()
    Thread(target=consumer, args=(cv,)).start()

    for _ in range(TOTAL_TASKS):
        Thread(target=producer, args=(cv,)).start()

