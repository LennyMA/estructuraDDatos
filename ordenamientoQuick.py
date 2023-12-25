def quickSort(a_list):
    quickSortHelper(a_list, 0, len(a_list) - 1)


def quickSortHelper(a_list, first, last):
    if first < last:
        splitPoint = partition(a_list, first, last)
        quickSortHelper(a_list, first, splitPoint - 1)
        quickSortHelper(a_list, splitPoint + 1, last)


def partition(a_list, first, last):
    pivotValue = a_list[first]
    leftMark = first + 1
    rightMark = last
    done = False
    while not done:
        while leftMark <= rightMark and a_list[leftMark] <= pivotValue:
            leftMark += 1
        while a_list[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark -= 1
        if rightMark < leftMark:
            done = True
        else:
            temp = a_list[leftMark]
            a_list[leftMark] = a_list[rightMark]
            a_list[rightMark] = temp
    temp = a_list[first]
    a_list[first] = a_list[rightMark]
    a_list[rightMark] = temp
    return rightMark

lista = [33, 5, 67, 1, 56, 9, 0, 78, 6, 12, 21, 30]
quickSort(lista)
print(lista)
