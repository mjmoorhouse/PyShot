#!/usr/bin/python
__author__ = 'Tutorials Point'

"""
Copied Verbatim from: http://www.tutorialspoint.com/python/python_multithreading.htm

Demonstrates the creation of two threads and executing them;
each prints the time after it has 'slept' 2s or 4s:

Gives this general type of output:

 Thread-1: Wed May  4 14:23:13 2016
 Thread-2: Wed May  4 14:23:15 2016
 Thread-1: Wed May  4 14:23:15 2016
 Thread-1: Wed May  4 14:23:17 2016
 Thread-2: Wed May  4 14:23:19 2016
 Thread-1: Wed May  4 14:23:19 2016

"""



import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass