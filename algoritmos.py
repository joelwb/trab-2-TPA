from data_struct import data_inf
import math
from random import randint


def is_sorted(a: list) -> bool:
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False

    return True


def __partition(a, p: int, r: int) -> int:
    pivot = a[r - 1]
    i = p

    for j in range(p, r):
        if pivot > a[j]:
            a[i], a[j] = a[j], a[i]
            i += 1

    if a[i] > pivot:
        a[i], a[r - 1] = a[r - 1], a[i]

    return i + 1


def insertion_sort(a: list) -> None:
    """
    Baseado no que foi implementado pelo professor em sala de aula,
    e também no pseudo-código disponivel no pdf na sala no AVA
    """

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


def selection_sort(a: list) -> None:
    """
    Baseado no que foi implementado pelo professor em sala de aula
    """

    for i in range(len(a)):
        pos_menor = i
        for j in range(i + 1, len(a)):
            if a[pos_menor] > a[j]:
                pos_menor = j

        a[i], a[pos_menor] = a[pos_menor], a[i]


def merge_sort(a: list) -> None:
    """
    Baseado no pseudo-código que está disponível na sala no AVA
    """

    def merge(p: int, q: int, r: int) -> None:
        n1 = q - p + 1
        n2 = r - q

        a1 = [a[p + i - 1] for i in range(1, n1)] + [data_inf]
        a2 = [a[q + i] for i in range(n2)] + [data_inf]

        i, j = 0, 0

        for k in range(p, r):
            if a1[i] <= a2[j]:
                a[k] = a1[i]
                i += 1
            else:
                a[k] = a2[j]
                j += 1

    def _merge_sort(p: int, r: int) -> None:
        if r - p > 1:
            q = (r + p) // 2
            _merge_sort(p, q)
            _merge_sort(q, r)
            merge(p, q, r)

    _merge_sort(0, len(a))


def quick_sort(a: list) -> None:
    """
    Baseado no que foi implementado pelo professor em sala de aula, e
    também no pseudo-código que está na Wikipédia - https://pt.wikipedia.org/wiki/Quicksort
    """

    def _quick_sort(p: int, r: int) -> None:
        if r - p > 1:
            pivot = __partition(a, p, r)
            _quick_sort(p, pivot - 1)
            _quick_sort(pivot, r)

    _quick_sort(0, len(a))


def heap_sort(a: list) -> None:
    """
    Baseado no algoritmo implementado em sala de aula,
    E também na video aula de link https://www.youtube.com/watch?v=mhQpxD_ThWM
    """

    def heapify(i: int):
        _left = 2 * i + 1
        _right = 2 * i + 2
        maior = i

        if _left < tamanho and a[_left] > a[maior]:
            maior = _left

        if _right < tamanho and a[_right] > a[maior]:
            maior = _right

        if maior != i:
            a[i], a[maior] = a[maior], a[i]
            heapify(maior)

    tamanho = len(a)
    for j in range(len(a) // 2, -1, -1):
        heapify(j)

    for j in range(len(a) - 1, 0, -1):
        tamanho = j
        a[0], a[tamanho] = a[tamanho], a[0]
        heapify(0)


def intro_sort(a: list):
    """
    Baseado no pseudo-código da Wikipédia - https://en.wikipedia.org/wiki/Introsort
    """

    def _intro_sort(p, r, max_depth):
        size = r - p + 1

        if size <= 1:
            return
        elif max_depth == 0:
            copy_a = a[p: r + 1]
            heap_sort(copy_a)
            a[p: r + 1] = copy_a
        else:
            pivot = __partition(a, p, r)
            _intro_sort(p, pivot - 1, max_depth - 1)
            _intro_sort(pivot, r, max_depth - 1)

    _intro_sort(0, len(a), int(math.log(len(a), 2)))


def tim_sort(a: list) -> None:
    """
    TimSort é um algoritmo que utiliza o Insertion Sort e o Merge Sort em conjunto
    """

    """
    O tamanho de divisão do array dá melhores resultados entre 32 e 64 (numeros que são potência de 2)
    """
    split_size_insertion = 32
    for i in range(0, len(a), split_size_insertion):
        interval = a[i: i + split_size_insertion]
        insertion_sort(interval)
        a[i: i + split_size_insertion] = interval
    # end for

    split_size_merge = split_size_insertion
    while split_size_merge < len(a):
        for i in range(0, len(a), split_size_merge * 2):
            interval = a[i: i + (2 * split_size_merge)]
            merge_sort(interval)
            a[i: i + (2 * split_size_merge)] = interval
        # end for
        split_size_merge = split_size_merge * 2


# a = [9, 7, 5, 3, 1, 8, 6, 4, 2]
# a = [randint(0, 10000000) for i in range(10000)]
# intro_sort(a)
# print(is_sorted(a))
