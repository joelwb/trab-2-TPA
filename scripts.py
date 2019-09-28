import os
from main import main
from func_timeout import func_timeout, FunctionTimedOut

def lenght_arqs():
    arqs = os.listdir("trab2-data")

    for path in arqs:
        arq = open(f"trab2-data/{path}")
        arq.readline()
        print(f"{path}: {len(arq.readlines())}")


def test():
    algoritmos = ["quick_sort", "merge_sort", "heap_sort", "insertion_sort", "selection_sort"]
    arqs = os.listdir("trab2-data")
    arqs.sort()
    for algoritmo in algoritmos:
        try:
            for arq in arqs:
                arq_teste = open(f"testes/{algoritmo}_{arq}", "w")
                print(f"{algoritmo} - {arq}")

                for num_exec in range(10):

                    tempo = func_timeout(400 * 10, main, args=(["-a", algoritmo, "-i", f"trab2-data/{arq}", "-o", f"trab2-output/{algoritmo}_{arq}"],))
                    arq_teste.write(f"{num_exec+1},{tempo}\n")

                arq_teste.close()
        except FunctionTimedOut:
            arq_teste.close()
            print(f"Timeout in {algoritmo} a partir do arq {arq}")
            continue

test()