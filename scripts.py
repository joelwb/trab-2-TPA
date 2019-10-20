import os
from main import main
from func_timeout import func_timeout, FunctionTimedOut
from matplotlib import pyplot as plt


def lenght_arqs():
    arqs = os.listdir("trab2-data")

    for path in arqs:
        arq = open(f"trab2-data/{path}")
        arq.readline()
        print(f"{path}: {len(arq.readlines())}")


def test():
    algoritmos = ["quick_sort", "merge_sort", "heap_sort", "insertion_sort", "selection_sort", "intro_sort", "tim_sort"]
    arqs = os.listdir("trab2-data")
    arqs.sort(key=lambda x: (x[8], x[5]))

    for algoritmo in algoritmos:
        if not os.path.exists(f"testes/{algoritmo}"):
            os.mkdir(f"testes/{algoritmo}")

        if not os.path.exists(f"trab2-output/{algoritmo}"):
            os.mkdir(f"trab2-output/{algoritmo}")

        try:
            for arq in arqs:
                if os.path.exists(f"testes/{algoritmo}/{arq}"):
                    continue

                arq_teste = open(f"testes/{algoritmo}/{arq}", "w")
                print(f"{algoritmo} - {arq}")

                tempos = []
                for num_exec in range(10):

                    tempo = func_timeout(400 * 10, main, args=(["-a", algoritmo, "-i", f"trab2-data/{arq}", "-o", f"trab2-output/{algoritmo}/{arq}"],))
                    arq_teste.write(f"{num_exec+1};{tempo}\n")
                    arq_teste.flush()
                    tempos.append(tempo)

                arq_teste.write(f"\nMédia,{sum(tempos) / len(tempos)}")
                arq_teste.close()
        except FunctionTimedOut:
            arq_teste.close()
            print(f"Timeout in {algoritmo} a partir do arq {arq}")
            continue


def create_csv_and_graphics_with_media():
    algs = os.listdir("testes")

    alg_color = {
        "quick_sort": "black",
        "merge_sort": "olive",
        "insertion_sort": "blue",
        "selection_sort": "red",
        "heap_sort": "magenta",
        "tim_sort": "green",
        "intro_sort": "aqua"
    }

    tamanho_arq = [10, 25, 50, 75]
    tamanho_arq += [tam * (10 ** i) for i in range(1, 6) for tam in tamanho_arq]

    medias_dict = {}

    for alg in algs:
        arq_saida = open(f"csv_graphics_media/{alg}.csv", "w")
        arq_saida.write("n,Media,Minimo,Maximo\n")
        arqs = os.listdir(f"testes/{alg}")
        arqs.sort(key=lambda x: (x[8], x[5]))

        medias = []
        for i, arq in enumerate(arqs):
            file = open(f"testes/{alg}/{arq}", "r")

            tempos = [float(file.readline().split(";")[1]) * 1000 for i in range(10)]
            media = sum(tempos)/len(tempos)
            minimo = min(tempos)
            maximo = max(tempos)
            medias.append(media)

            file.close()
            arq_saida.write(f"{tamanho_arq[i]},{media:.2f},{minimo:.2f},{maximo:.2f}\n")

        arq_saida.close()

        plt.xlabel("n")
        plt.ylabel("Médias")
        plt.xticks([0, 100000, 500000, 1000000, 2500000, 5000000, 7500000], rotation='vertical')
        plt.title(alg)
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        plt.subplots_adjust(bottom=0.15)
        plt.plot(tamanho_arq[:len(medias)], medias, color=alg_color[alg])
        plt.savefig(f"csv_graphics_media/{alg}.png")
        plt.clf()

        medias_dict[alg] = medias

    for alg, medias in medias_dict.items():
        plt.xlabel("n")
        plt.ylabel("Médias")
        plt.title("Todos Algoritmos")
        plt.xticks([0, 50000, 100000, 250000, 500000], rotation='vertical')
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        plt.xlim(0, 500000)
        plt.plot(tamanho_arq[:len(medias)], medias, label=alg, color=alg_color[alg])
        plt.legend()
        plt.savefig("csv_graphics_media/all_reduced.png")

    for alg, medias in medias_dict.items():
        plt.xlabel("n")
        plt.ylabel("Médias")
        plt.title("Todos Algoritmos")
        plt.xticks([0, 100000, 500000, 1000000, 2500000, 5000000, 7500000], rotation='vertical')
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
        plt.plot(tamanho_arq[:len(medias)], medias, label=alg, color=alg_color[alg])
        plt.savefig("csv_graphics_media/all.png")


create_csv_and_graphics_with_media()