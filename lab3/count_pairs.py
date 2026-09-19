import random

def count_pairs(arr, target):
    seen = set()
    count = 0

    for x in arr:
        complement = target - x

        if complement in seen:
            count += 1

        seen.add(x)

    return count


random.seed(42)
N = 50000       # change to 50000 for the second run
arr = [random.randint(1, 20000) for _ in range(N)]
target = 20000

print("Number of pairs:", count_pairs(arr, target))