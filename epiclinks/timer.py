import time
import sys


def timer():
    i = 3600
    while i > 0:
      sys.stdout.write("\r%d" % i)
      sys.stdout.flush()
      i = i - 1
      time.sleep(1)

