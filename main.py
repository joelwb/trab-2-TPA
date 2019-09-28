from algoritmos import merge_sort, insert_sort, selection_sort, is_sorted
from time import time
from datetime import date
from data_struct import Data


def main():
    arq = open("trab2-data/data_75e3.csv", "r")
    arq.readline()
    datas = [Data(line[0], line[1], line[2], date.fromisoformat(line[3]), int(line[4]), int(line[5])) for line in (line_str.split(",") for line_str in arq.readlines())]
    print(len(datas))
    start = time()
    #merge_sort(datas, 0, len(datas))
    #insert_sort(datas)
    selection_sort(datas)
    #print(datas)
    print(time() - start)
    print(is_sorted(datas))


main()