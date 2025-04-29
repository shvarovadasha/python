import random
import time

from bubble import bubble_sort
from heap import heap_sort
from insertion import insertion_sort
from merge import merge_sort
from quick import quick_sort
from selection import selection_sort

# Словарь: название → функция сортировки
algorithms = {
    "bubble": bubble_sort,
    "heap": heap_sort,
    "insert": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "selection": selection_sort,
    "builtin": sorted
}

# Размеры массивов
sizes = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]
repeats = 10

def measure_time(sort_func, data):
    times = []
    for _ in range(repeats):
        x = data.copy()
        start = time.perf_counter()
        if sort_func == sorted:  # встроенная сортировка возвращает список
            sort_func(x)
        else:
            sort_func(x)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / repeats

if __name__ == "__main__":
    print("algorithm,size,avg_time_seconds")
    for name, func in algorithms.items():
        for size in sizes:
            data = [random.randint(0, 1000) for _ in range(size)]
            avg_time = measure_time(func, data)
            print(f"{name},{size},{avg_time:.6f}")
