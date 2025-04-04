
import time

class SortingAlgorithms:
    
    @staticmethod
    def selection_sort(arr):
        arr = arr[:]  # Copie pour éviter de modifier la liste originale
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def bubble_sort(arr):
        arr = arr[:]
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def insertion_sort(arr):
        arr = arr[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def merge_sort(arr):
        arr = arr[:]
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_half = SortingAlgorithms.merge_sort(left_half)
            right_half = SortingAlgorithms.merge_sort(right_half)

            return SortingAlgorithms.merge(left_half, right_half)
        return arr
    
    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def quick_sort(arr):
        arr = arr[:]
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

    @staticmethod
    def heap_sort(arr):
        arr = arr[:]
        n = len(arr)

        # Construire un tas max
        for i in range(n//2 - 1, -1, -1):
            SortingAlgorithms.heapify(arr, n, i)

        # Extraire les éléments du tas
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Échanger
            SortingAlgorithms.heapify(arr, i, 0)
        return arr

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms.heapify(arr, n, largest)

    @staticmethod
    def comb_sort(arr):
        arr = arr[:]
        n = len(arr)
        gap = n
        shrink = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            i = 0
            while i + gap < n:
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted = False
                i += 1
        return arr

    @staticmethod
    def measure_time(sort_function, arr):
        start_time = time.time()
        sorted_arr = sort_function(arr)
        end_time = time.time()
        return sorted_arr, end_time - start_time

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]

# Mesurer le temps d'exécution de chaque algorithme
algorithms = [SortingAlgorithms.selection_sort, SortingAlgorithms.bubble_sort, SortingAlgorithms.insertion_sort,
              SortingAlgorithms.merge_sort, SortingAlgorithms.quick_sort, SortingAlgorithms.heap_sort, SortingAlgorithms.comb_sort]

for algo in algorithms:
    sorted_list, duration = SortingAlgorithms.measure_time(algo, liste)
    print(f"Liste triée avec {algo.__name__} : {sorted_list}")
    print(f"Temps d'exécution : {duration:.6f} secondes\n")
