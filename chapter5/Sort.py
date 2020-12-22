from pprint import pprint


def bubbleSort(alist: list) -> None:
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def shortBubbleSort(alist: list) -> None:
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1


def selectionSort(alist: list) -> None:
    for fillslot in range(len(alist) - 1, 0, -1):
        postionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[postionOfMax]:
                postionOfMax = location

        alist[fillslot], alist[postionOfMax] = alist[postionOfMax], alist[fillslot]


def insertionSort(alist: list):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


def shellSort(alist: list):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is ", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue


def mergeSortStart(alist: list):
    tempList = [0] * len(alist)
    mergeSort(alist, tempList, 0, len(alist) - 1)


def mergeSort(alist: list, tempList: list, start: int, end: int) -> None:
    if start < end:
        center = (start + end) // 2
        print("Splitting ", alist[start : center + 1])
        mergeSort(alist, tempList, start, center)
        print("Splitting ", alist[center + 1 : end + 1])
        mergeSort(alist, tempList, center + 1, end)
        merge(alist, tempList, start, center + 1, end)


def merge(alist: list, tempList: list, start: int, center: int, end: int) -> None:
    leftEnd = center - 1
    left = start
    right = center
    tmpPos = start
    while left <= leftEnd and right <= end:
        if alist[left] < alist[right]:
            tempList[tmpPos] = alist[left]
            left = left + 1
        else:
            tempList[tmpPos] = alist[right]
            right = right + 1
        tmpPos = tmpPos + 1

    while left <= leftEnd:
        tempList[tmpPos] = alist[left]
        left = left + 1
        tmpPos = tmpPos + 1

    while right <= end:
        tempList[tmpPos] = alist[right]
        right = right + 1
        tmpPos = tmpPos + 1

    for i in range(start, end + 1):
        alist[i] = tempList[i]
    print("Merging ", alist[start : end + 1])


def quickSort(alist: list) -> None:
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist: list, first: int, last: int) -> None:
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)


def partition(alist: list, first: int, last: int) -> int:
    pivotValue = alist[first]
    leftMark = first + 1
    rightMark = last
    done = False
    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1
        while rightMark >= leftMark and alist[rightMark] >= pivotValue:
            rightMark -= 1

        if rightMark < leftMark:
            done = True
        else:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

    alist[first], alist[rightMark] = alist[rightMark], alist[first]
    return rightMark


alist = [5, 6, 8, 7, 2, 1]
quickSort(alist)
pprint(alist)