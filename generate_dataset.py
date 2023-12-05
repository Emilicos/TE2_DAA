from enum import Enum
import random, os

class DATASET(Enum):
    SMALL = 20
    MEDIUM = 200
    BIG = 2000

def write_to_file(sets, costs, filename):
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    with open(filename, "w") as file:
        for i in range(len(sets)):
            for j, item in enumerate(sets[i]):
                if(j == len(sets[i])-1):
                    file.write(f'{item}\n')
                    if(i == len(sets)-1):
                        file.write(f'{costs[i]}')
                    else:
                        file.write(f'{costs[i]}\n')
                else:
                    file.write(f'{item} ')

def generate_random_set(size, low, high):
    return {random.randint(low, high) for _ in range(size)}
  
def generate_dataset(variance: str):
    set_sizes = [10, 15, 20]
    
    if variance == "small":
        size = 20
    elif variance == "medium":
        size = 200
    elif variance == "big":
        size = 2000
    else:
        raise ValueError("Invalid variance parameter. Use 'small', 'medium', or 'big'.")
    
    universe = set(range(1, size+1))

    for set_size in set_sizes:
        sets = []
        test_set = set()
        while test_set != universe:
            sets = []
            test_set = set()
            for k in range(set_size):
                size_range = max(1, random.randint(size // set_size, size // 2))

                random_set = generate_random_set(size_range, 1, size)                
                sets.append(random_set)
                test_set |= random_set # Union x
                
        costs = [random.randint(1, 50) for _ in range(set_size)]
        write_to_file(sets, costs, f'dataset/{variance}/{set_size}.txt')
        
def main():
    generate_dataset("small")
    generate_dataset("medium")
    generate_dataset("big")
    
if __name__ == '__main__':
    main()