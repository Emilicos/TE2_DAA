import tracemalloc
import time
import copy
import numpy as np
from branch_and_bound import BB
from generate_dataset import DATASET
from greedy import set_cover

types = ["small", "medium"]
set_sizes = [10, 15, 20]

def WeightedSetCoverUsingGreedy(universe, subsets, costs, array_type):
    tracemalloc.start()
    start_time = time.time()
    cover = set_cover(universe, subsets, costs)
    assert cover is not None
    end_time = time.time()
    # menggunakan peak memory
    used = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()
    
    print(f"Weighted Set Cover dengan algoritma Greedy dengan {array_type} cost nya {cover[1]}")
    print(f"Weighted Set Cover dengan algoritma Greedy dengan {array_type} menghabiskan {used:.10f} KB.")
    delta = (end_time - start_time) * 1000
    print(f"Weighted Set Cover dengan algoritma Greedy dengan {array_type} menghabiskan {delta:.10f} ms. \n\n")

def WeightedSetCoverUsingBranchAndBound(universe, subsets, costs, array_type):
    tracemalloc.start()
    start_time = time.time()
    # tidak disimpan di variabel agar waktu assigmment tidak dihitung
    cover = BB(universe, subsets, costs)
    end_time = time.time()
    # menggunakan peak memory
    used = tracemalloc.get_traced_memory()[1]/1024
    tracemalloc.stop()
    
    print(f"Weighted Set Cover dengan algoritma Branch and Bound dengan {array_type} cost nya {cover[0]}")


    print(f"Weighted Set Cover dengan algoritma Branch and Bound dengan {array_type} menghabiskan {used:.10f} KB.")
    
    delta = (end_time - start_time) * 1000
    print(f"Weighted Set Cover dengan algoritma Branch and Bound dengan {array_type} menghabiskan {delta:.10f} ms.\n\n")
   
def main():
    print("Perbandingan Algoritma Greedy dan Branch and Bound pada Weighted Set Cover Problem")
    print("="*100)
    
    universe = set()
    
    for type in types:
        for set_size in set_sizes:
            sets = []
            costs = []
            counter = 0
            with open(f'dataset/{type}/{set_size}.txt', 'r') as file:
                for line in file:
                    A = [int(x) for x in line.split()]
                    
                    if(counter % 2 == 0):
                        sets.append(set(A[:]))
                    else:
                        costs.append(A[0])
                    
                    counter += 1
            
            if(type == "small"):
                m = DATASET.SMALL.value
            elif(type == "medium"):
                m = DATASET.MEDIUM.value
            elif(type == "big"):
                m = DATASET.BIG.value
                
            universe = set(range(1, m+1)) # set dari semua elemen
                            
            WeightedSetCoverUsingGreedy(universe, sets, costs, type)
            
            WeightedSetCoverUsingBranchAndBound(universe, sets, costs, type)

    return True

if __name__ == '__main__':
    main()