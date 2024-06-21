#!/usr/bin/env python3
'''file to generate for stdin'''
from random import randint, random, choice
from time import sleep
from datetime import datetime
from sys import stdout


stat_code = [200, 301, 400, 401, 403, 404, 405, 500]
for i in range(1000):
    sleep(random())
    stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
           randint(1, 255), randint(1, 255), randint(1, 255), randint(1, 255),
           datetime.now(), choice(stat_code),
           randint(1, 1024)
))
    stdout.flush()
