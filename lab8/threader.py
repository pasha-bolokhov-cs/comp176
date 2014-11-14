#!/usr/bin/env python


import threading, time, random, sys

MIN_SLEEP = 1   # minimum how long to sleep for
MAX_SLEEP = 8   # maximum how long to sleep for


# a lock for printing
plock = threading.Condition()

# a lock for waiting
wlock = threading.Condition()


def counter():
    # sleep for up to MAX_SLEEP seconds
    s = random.randrange(MIN_SLEEP, MAX_SLEEP + 1)
    time.sleep(s)

    # now report
    name = threading.currentThread().getName()
    plock.acquire()
    sys.stdout.write("Thread `%s' has slept for %d seconds\n" % (name, s))
    plock.notify()
    plock.release()




def main():
    
    sys.stdout.write("Give me the number of threads to create: ")
    num = int(sys.stdin.readline().rstrip('\n'))

    # start 'num' threads
    for n in xrange(num):
        t = threading.Thread(name="worker " + str(n), target=counter)
        t.start()

    # wait for them to complete
    while (threading.activeCount() > 1):
        plock.acquire()
        plock.wait()                # wait for notification
        plock.release()

    # report completion
    sys.stdout.write("Main thread complete (activeCount() = %d)\n" % threading.activeCount())




#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()


