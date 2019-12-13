def Parent(k):
    if k <= 0:
        return None
    return (k-1) // 2


def Left(k):
    if k < 0:
        return None
    return k*2+1


def Right(k):
    if k < 0:
        return None
    return k*2+2


def Max_Heapify(data, k, size):
    left = Left(k)
    right = Right(k)

    if (not left) or (not right) or size <= 1:
        return

    exchange_index = k
    max_elem = data[k]

    if left < size and max_elem < data[left]:
        exchange_index = left
        max_elem = data[left]

    if right < size and max_elem < data[right]:
        exchange_index = right
        max_elem = data[right]

    if exchange_index != k:
        data[k], data[exchange_index] = data[exchange_index], data[k]
        Max_Heapify(data, exchange_index, size)


def Build_Max_Heap(data):
    size = len(data)

    if size <= 1:
        return

    cursor = Parent(size-1)

    while cursor >= 0:
        Max_Heapify(data, cursor, size)
        cursor = cursor - 1


def Heap_Sort(data):
    Build_Max_Heap(data)  # 建堆O(n)

    size = len(data)
    cursor = size - 1
    while cursor >= 1:
        data[0], data[cursor] = data[cursor], data[0]
        Max_Heapify(data, 0, cursor)
        cursor = cursor - 1


if __name__ == '__main__':
    a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    Heap_Sort(a)
    print(a)
