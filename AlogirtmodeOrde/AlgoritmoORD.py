#QuickSort

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending Order:")
print(data)

#Mergesort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Llamada recursiva para ordenar ambas mitades
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Combinar las mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Agregar los elementos restantes (si los hay)
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Ejemplo de uso
mi_lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista original:", mi_lista)
mi_lista_ordenada = merge_sort(mi_lista)
print("Lista ordenada:", mi_lista_ordenada)

#Shellsort

def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Ejemplo de uso
mi_lista = [12, 34, 54, 2, 3]
print("Lista original:", mi_lista)
shellSort(mi_lista)
print("Lista ordenada:", mi_lista)

#Heapsort

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

# Ejemplo de uso
arr = [12, 34, 54, 2, 3, 10, 9, 1]
print("Original array:", arr)
arr = heapsort(arr)
print("Sorted array:", arr)

#Hashing

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count_arr = [0 for _ in range(range_val)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr)):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    return output_arr

# Ejemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)
arr = counting_sort(arr)
print("Sorted array:", arr)
