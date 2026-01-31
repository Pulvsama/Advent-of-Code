from typing import List, Optional, Tuple, Union
from pathlib import Path
import random
import time
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = SCRIPT_DIR / "input.txt"
TARGET_SUM = 2020

def load_numbers(filepath: Union[str, Path]) -> List[int]:
    """Reads whitespace-separated integers from a file."""
    with open(filepath) as f:
        return [int(x) for x in f.read().split()]
    
def generate_test_case_2(length: int, target: int) -> Tuple[List[int], int]:
    """
    Generates a list of random integers. 
    Guarantees that exactly one pair sums up to the target.
    """
    if length < 2:
        raise ValueError("List length must be at least 2")
    
    numbers = [random.randint(target//2 + 1, target * 2) for _ in range(length - 2)]
    n1 = random.randint(0, target)
    n2 = target - n1
    numbers.extend([n1, n2])
    random.shuffle(numbers)
    return numbers, n1 * n2

def generate_test_case_3(length: int, target: int) -> Tuple[List[int], int]:
    """
    Generates a list of random integers. 
    Guarantees that exactly one triplet sums up to the target.
    """
    if length < 3:
        raise ValueError("List length must be at least 3")
    
    numbers = [random.randint(target // 2 + 1, target * 2) for _ in range(length - 3)]
    n1 = random.randint(0, target)
    n2 = random.randint(0, target - n1)
    n3 = target - n1 - n2
    numbers.extend([n1, n2, n3])
    random.shuffle(numbers)
    return numbers, n1 * n2 * n3

def find_two_sum_set(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target."""
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None

def find_two_sum_brute_force(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target. 
    Using brute force, the complexity will be in O(n^2)"""
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None

def find_three_sum(target: int, numbers: List[int]) -> Optional[Tuple[int, int, int]]:
    """Finds a triplet of numbers that sum to the target"""
    for number in numbers:
        complement = target - number
        residual = numbers.copy()
        residual.remove(number)
        res_two_sum = find_two_sum_set(complement, residual)
        if res_two_sum:
            return (number, res_two_sum[0], res_two_sum[1])
    return None

if __name__ == "__main__":
    "Compare the time it takes for both methods of two-sums"
    times_brute_force = []
    times_set = []
    times = []
    lengths = [3, 100, 1000, 2000, 5000, 10000, 20000, 50000]
    for length in lengths:
        numbers, result = generate_test_case_2(length, 2020)
        start_time = time.time()
        brute_force_pair = find_two_sum_brute_force(2020, numbers)
        end_time = time.time()
        brute_force_res = brute_force_pair[0] * brute_force_pair[1] if brute_force_pair else -1
        if brute_force_res == result:
            times_brute_force.append(end_time - start_time)
        else:
            raise ValueError(f"Wrong result, brute force method, got {brute_force_res} instead of {result}")
        start_time = time.time()
        set_pair = find_two_sum_set(2020, numbers)
        end_time = time.time()
        set_res = set_pair[0] * set_pair[1] if set_pair else -1
        if set_res == result:
            times_set.append(end_time - start_time)
        else:
            raise ValueError(f"Wrong result, set method, got {set_res} instead of {result}")
        
    "Same test on the only algorithm for three-sum"
    for length in lengths:
        numbers, result = generate_test_case_3(length, 2020)
        start_time = time.time()
        triplet = find_three_sum(2020, numbers)
        end_time = time.time()
        res = triplet[0] * triplet[1] * triplet[2] if triplet else -1
        if res == result:
            times.append(end_time - start_time)
        else:
            raise ValueError(f"Wrong result, three-sum, got {res} instead of {result}")
    
    plt.plot(lengths, times_set, label="Set method", color="r")
    plt.plot(lengths, times_brute_force, label="Brute force method", color="b")
    plt.plot(lengths, times, label="Three-sum", color="g")
    plt.legend()
    plt.show()