#Michael Lannon
from finch import Finch
from time import sleep
myFinch = Finch()
def dance1():
    snakyFinch = Finch()
    for i in range(5):
        snakyFinch.wheels(1, 1)
        sleep(1)
        snakyFinch.wheels(0, 1)
        sleep(1)
        snakyFinch.wheels(1, 0)
        sleep(1)
        snakyFinch.wheels(-1, -1)
        sleep(0.5)
        snakyFinch.wheels(0.2, -1)
        sleep(1)
        snakyFinch.wheels(0.3, 0.3)
        sleep(2.5)
        if i == 4:
            snakyFinch.close();

def dance2():
    snakyFinch = Finch()
    for i in range(5):
        snakyFinch.wheels(1, 1)
        sleep(1)
        snakyFinch.wheels(0, -1)
        sleep(1)
        snakyFinch.wheels(1, 0)
        sleep(1)
        snakyFinch.wheels(1, -1)
        sleep(0.5)
        snakyFinch.wheels(0.5, 1)
        sleep(1)
        snakyFinch.wheels(0.75, -0.3)
        sleep(2.5)
        if i == 4:
            snakyFinch.close();

def dance3():
    snakyFinch = Finch()
    for i in range(5):
        snakyFinch.wheels(1, 0)
        sleep(1)
        snakyFinch.wheels(-1, 1)
        sleep(1)
        snakyFinch.wheels(1, 0)
        sleep(1)
        snakyFinch.wheels(-1, 0)
        sleep(0.5)
        snakyFinch.wheels(-0.9, 1)
        sleep(1)
        snakyFinch.wheels(0.75, 0.2)
        sleep(2.5)
        if i == 4:
            snakyFinch.close();