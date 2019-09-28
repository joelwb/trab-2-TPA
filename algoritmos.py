from data_struct import data_inf


def is_sorted(a: list) -> bool:
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                return False

    return True


def insert_sort(a: list) -> None:
    for i in range(1, len(a)):
        v = a[i]
        j = i - 1

        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = v


def selection_sort(a: list) -> None:
    for i in range(len(a)):
        pos_menor = i
        for j in range(i+1, len(a)):
            if a[pos_menor] > a[j]:
                pos_menor = j

        a[i], a[pos_menor] = a[pos_menor], a[i]


def merge_sort(a: list) -> None:

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
    def partition(p: int, r: int) -> int:
        pivot = a[r - 1]
        i = p

        for j in range(p, r):
            if pivot > a[j]:
                a[i], a[j] = a[j], a[i]
                i += 1

        if a[i] > pivot:
            a[i], a[r - 1] = a[r - 1], a[i]

        return i+1

    def _quick_sort(p: int, r: int) -> None:
        if r - p > 1:
            pivot = partition(p, r)
            _quick_sort(p, pivot-1)
            _quick_sort(pivot, r)

    _quick_sort(0, len(a))