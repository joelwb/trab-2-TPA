from algoritmos import merge_sort, insertion_sort, selection_sort, quick_sort, heap_sort, is_sorted
from time import time
from datetime import date
from data_struct import Data
import argparse


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',
                        choices=["quick_sort", "merge_sort", "heap_sort", "insertion_sort", "selection_sort"],
                        required=True,
                        dest="algoritmo",
                        help="Algoritmo a ser usado")

    parser.add_argument("-i", dest="input_file", help="Input file", required=True)
    parser.add_argument("-o", dest="output_file", help="Output file", required=True)
    args = parser.parse_args(args)

    arq_input = open(args.input_file, "r")
    arq_input.readline()

    datas = [Data(line[0], line[1], line[2], date.fromisoformat(line[3]), int(line[4]), int(line[5])) for line in (line_str.split(",") for line_str in arq_input.readlines())]
    arq_input.close()

    start = time()
    exec(f"{args.algoritmo}(datas)")
    tempo_gasto = time() - start

    """
    arq_output = open(args.output_file, "w")
    arq_output.write("email,gender,uid,birthdate,height,weight")
    arq_output.writelines([str(data)+"\n" for data in datas])
    """

    print(tempo_gasto)

    #print(is_sorted(datas))
    return tempo_gasto