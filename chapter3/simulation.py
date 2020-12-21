from random import randrange
from Queue import Queue
from Printer import Printer
from Task import Task


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print(
        "Average Wait %6.2f secs %3d tasks remaining."
        % (averageWait, printQueue.size())
    )


def newPrintTask():
    num = randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def main():
    for i in range(10):
        simulation(3600, 10)


if __name__ == "__main__":
    main()