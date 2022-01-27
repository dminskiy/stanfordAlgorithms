import time
from utils import read_file_into_array


def SortAndCount(arr):

    #Notes: https://docs.google.com/document/d/1RDaA2t7z9vNKXRehf8FfxtL7gBx-9Rd6bOoshE4TRQE/

    n = len(arr)
    if n == 1:
        return arr, 0

    B, x = SortAndCount(arr[:int(n/2)])
    C, y = SortAndCount(arr[int(n/2):])
    D, z = MergeAndCountSplitInv(B, C)

    return D, x+y+z


def MergeAndCountSplitInv(B, C):
    i = 0
    j = 0
    inversion_count = 0
    out_arr = [None]*len(B) + [None]*len(C)

    for k in range(len(out_arr)):
        # Check B
        if i < len(B):       # B non-empty
            if j >= len(C):  # C is empty
                out_arr[k] = B[i]
                i += 1
            elif B[i] <= C[j]:  # C non-empty, B non-empty -> copy B if B[i] <= C[j]
                out_arr[k] = B[i]
                i += 1
            else:  # if B non-empty, C non empty -> copy C if B[i] > C[j]
                out_arr[k] = C[j]
                inversion_count += len(B) - i
                j += 1
        # Copy C if B is empty
        else:
            out_arr[k] = C[j]
            inversion_count += len(B) - i
            j += 1

    return out_arr, inversion_count


if __name__ == '__main__':
    print('Let us count the number of MergeSort inversions!')

    arr = read_file_into_array('IntegerArray.txt')

    s = time.time()
    sorted_arr, num_inversions = SortAndCount(arr)
    proc_t = time.time() - s

    print(f'Calculating the number of inversions.\nResult: {num_inversions}\nExecution time: {round(proc_t, 5)}s')
