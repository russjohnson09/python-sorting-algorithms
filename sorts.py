from random import shuffle
def mergesort(w):
    if len(w) < 2:
        return w
    else:
        mid = len(w) // 2
        return merge(mergesort(w[:mid]),mergesort(w[mid:]))

def merge(x,y):
    result = []
    i,j = 0,0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    result += x[i:]
    result += y[j:]
    return result

def qsort(w):
    if len(w) < 2:
        return w
    else:
        pivot = w[0]
        left, right = [], []
        for x in w[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return qsort(left) + [pivot] + qsort(right)

#bubblesort (aka best sorting algorithm evaa)
def bubble(w):
    n = len(w)
    i = 1
    for j in range(len(w), 0, -1):
        for i in range(1,j):
            if w[i] < w[i-1]:
                w[i], w[i-1] = w[i-1], w[i]
    return w

#nevermind about that bogo is best
def bogo(w):
    while not all(x <= y for x, y in zip(w, w[1:])):
        shuffle(w)
    return w

def insertsort(w):
    for i in range(1, len(w)):
        for j in range(i, 0, -1):
            if w[j] < w[j-1]:
                w[j], w[j-1] = w[j-1], w[j]
            else:
                break
    return w




