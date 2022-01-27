import os

DATA_PATH = '/home/dm00314/PycharmProjects/stanfordAlgorithms/Divide&Conquer,Algorithms/data'

def read_file_into_array(filename):
    filepath = os.path.join(DATA_PATH, filename)
    if os.path.exists(filepath):
        file = open(filepath, 'r')
        lines = file.readlines()
        arr = [int(lines[i]) for i in range(len(lines))]
        return arr
    else:
        return None