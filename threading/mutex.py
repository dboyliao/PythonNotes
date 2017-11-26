#!/usr/bin/env python3
# -*- coding:utf8 -*-
from __future__ import print_function
import sys
from threading import Lock, Thread
from time import sleep
from random import random

mutex = Lock()

class Worker(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        sleep(random()*3)
        # try block here is essential since that if the mutex is acquired,
        # and some exception is throwed, the mutex will not be released and
        # all threads block
        try:
            mutex.acquire()
            print("[{}] mutex acquired!".format(self.name), flush=True)
            for _ in range(3):
                print("{} is working".format(self.name), flush=True)
                if random() < 0.2:
                    raise ValueError("{} fails".format(self.name))
        finally:
            print("[{}] mutex release".format(self.name), flush=True)
            mutex.release()


def main():

    for i in range(5):
        t = Thread(target=Worker("worker_{}".format(i)))
        t.start()
    return 0


if __name__ == "__main__":
    sys.exit(main())
