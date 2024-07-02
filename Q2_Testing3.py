import random
import time
from collections import defaultdict


def generate_random_ic():
    return ''.join(random.choices('0123456789', k=12))


def custom_hash_function(icNumber):
    sumOfChar = 0
    array1 = []
    totalSum = 0
    hashCode = 0
    constantPrimeNumber = 7

    part1 = int(icNumber[0:3])
    part2 = int(icNumber[3:6])
    part3 = int(icNumber[6:9])
    part4 = int(icNumber[9:12])
    array1.append(part1)
    array1.extend([part2, part3, part4])

    for elements in array1:
        for char in str(elements):
            index = str(elements).index(char)
            sumOfChar += ord(char) * (int(char) * index)

        totalSum += sumOfChar

    # print(totalSum)
    tableSize = 3001
    hashCode = (totalSum * constantPrimeNumber) % tableSize

    return hashCode


def given_hash_function(ic_number):
    return int(ic_number) % 3001


def insert_into_hash_table(hash_table, ic_number, hash_function):
    index = hash_function(ic_number)
    if hash_table[index] is None:
        hash_table[index] = [ic_number]
    else:
        hash_table[index].append(ic_number)


def create_hash_table(size):
    return [None] * size


def measure_performance(hash_function, ic_numbers):
    hash_table_size = 3001
    hash_table = create_hash_table(hash_table_size)
    start_time = time.time()
    for ic in ic_numbers:
        insert_into_hash_table(hash_table, ic, hash_function)
    end_time = time.time()
    elapsed_time = end_time - start_time

    chain_lengths = [len(chain) for chain in hash_table if chain]
    num_non_empty_chains = len(chain_lengths)
    average_chain_length = sum(chain_lengths) / num_non_empty_chains if num_non_empty_chains > 0 else 0
    max_chain_length = max(chain_lengths) if chain_lengths else 0

    return elapsed_time, num_non_empty_chains, average_chain_length, max_chain_length


def main():
    num_ic_numbers = 2000
    num_experiments = 10
    hash_table_size = 3001

    # Generate 2000 random 12-digit IC numbers
    ic_numbers = [generate_random_ic() for _ in range(num_ic_numbers)]

    custom_results = defaultdict(list)
    given_results = defaultdict(list)

    for _ in range(num_experiments):
        elapsed_time, num_non_empty_chains, avg_chain_length, max_chain_length = measure_performance(
            custom_hash_function, ic_numbers)
        custom_results['elapsed_time'].append(elapsed_time)
        custom_results['num_non_empty_chains'].append(num_non_empty_chains)
        custom_results['avg_chain_length'].append(avg_chain_length)
        custom_results['max_chain_length'].append(max_chain_length)

        elapsed_time, num_non_empty_chains, avg_chain_length, max_chain_length = measure_performance(
            given_hash_function, ic_numbers)
        given_results['elapsed_time'].append(elapsed_time)
        given_results['num_non_empty_chains'].append(num_non_empty_chains)
        given_results['avg_chain_length'].append(avg_chain_length)
        given_results['max_chain_length'].append(max_chain_length)

    def report_results(results, function_name):
        print(f"\nResults for {function_name}:")
        print(f"Average time taken: {sum(results['elapsed_time']) / num_experiments:.6f} seconds")
        print(f"Average number of non-empty chains: {sum(results['num_non_empty_chains']) / num_experiments:.2f}")
        print(f"Average chain length: {sum(results['avg_chain_length']) / num_experiments:.2f}")
        print(f"Maximum chain length: {sum(results['max_chain_length']) / num_experiments:.2f}")

    report_results(custom_results, "Custom Hash Function")
    report_results(given_results, "Given Hash Function")


if __name__ == "__main__":
    main()
