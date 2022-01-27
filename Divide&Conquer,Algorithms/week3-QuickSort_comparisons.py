from utils import read_file_into_array
import time


def quickSort(_array, pivot_type):
    """
    return:
        int - number of comparisons
        array - sorted array
    """
    n = len(_array)
    if n <= 1:
        return 0, _array
    elif n == 2:
        if _array[0] > _array[1]:
            swap(_array, 0, 1)
        return 1, _array

    p_ind = chosePivot(_array, pivot_type)  # p_ind - index of the pivot point
    p_ind = partition(_array, p_ind)  # once partitioned, both p and array expected to change

    count1, sorted1 = quickSort(_array[:p_ind], pivot_type)
    count2, sorted2 = quickSort(_array[p_ind+1:], pivot_type)
    comparisons = len(_array) - 1 + count1 + count2

    return comparisons, sorted1+[_array[p_ind]]+sorted2


def chosePivot(_array, type: int):
    """
        type - pivot selection algorythm:
            0 -> first array element
            1 -> last array element
            2 -> median of three

        return:
            int - array index that will be used a pivot
    """

    assert type < 3

    if type == 0:
        return 0
    elif type == 1:
        return len(_array)-1
    else:
        l = 0
        r = len(_array)-1
        mid = l + (r - l) // 2
        if _array[l] > _array[mid]:
            if _array[l] < _array[r]:
                return l
            elif _array[mid] > _array[r]:
                return mid
            else:
                return r
        else:
            if _array[l] > _array[r]:
                return l
            elif _array[mid] < _array[r]:
                return mid
            else:
                return r


def partition(_array, p_ind):
    # make sure pivot is at 0
    swap(_array, p_ind, 0)

    left = 0
    right = len(_array)
    i = left + 1

    for j in range(left+1, right):
        # array 0 - pivot value
        if _array[j] < _array[0]:
            if i != j:
                swap(_array, i, j)
            i += 1

    p_ind = i - 1
    if p_ind != 0:
        swap(_array, 0, p_ind)
    return p_ind


def swap(_arr, ind1, ind2):
    temp1 = _arr[ind1]
    _arr[ind1] = _arr[ind2]
    _arr[ind2] = temp1


if __name__ == '__main__':
    print('Let us count the number of QuickSort comparisons!')

    arr = read_file_into_array(filename='QuickSort.txt')

    qs_start = time.time()

    comp, sorted = quickSort(arr, pivot_type=2)

    print(f'Calculating the number of comparisons.\nResult: {comp}'
          f'\nExecution time: {round(time.time()-qs_start, 5)}s')
    #print(f'Sorted array: {sorted}')
