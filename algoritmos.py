from data_struct import data_inf


def is_sorted(a: list) -> bool:
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                return False

    return True


def insert_sort(a: list):
    for i in range(1, len(a)):
        v = a[i]
        j = i - 1

        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = v


def selection_sort(a: list):
    def swap(a: list, i: int, j: int):
        aux = a[i]
        a[i] = a[j]
        a[j] = aux

    for i in range(len(a)):
        pos_menor = i
        for j in range(i+1, len(a)):
            if a[pos_menor] > a[j]:
                pos_menor = j

        swap(a, i, pos_menor)


def merge_sort(a: list, p: int, r: int) -> None:
    def merge(a: list, p: int, q: int, r: int) -> None:
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

    if r - p > 1:
        q = (r + p) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        merge(a, p, q, r)