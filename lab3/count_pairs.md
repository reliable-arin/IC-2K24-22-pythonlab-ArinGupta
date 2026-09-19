# Pair Sum Performance Analysis

## Step 1: Naive Version

Given a list of `N` integers and a target sum, count how many pairs of elements, by index, add up exactly to the target. Duplicates count separately.

The naive solution checks every possible pair using two nested loops.

### Test Cases

| Input List        | Target | Expected Output |
| ----------------- | -----: | --------------: |
| `[2, 7, 11, 15]`  |    `9` |             `1` |
| `[1, 1, 1]`       |    `2` |             `3` |
| `[3, 3, 4, 4]`    |    `7` |             `4` |
| `[5, 5, 5, 5, 5]` |   `10` |            `10` |
| `[1, 2, 3, 4, 5]` |  `100` |             `0` |

### Timing Setup

Use this exact code so that the input list is the same for each run:

```python
import random

random.seed(42)

N = 5000       # change to 50000 for the second run

arr = [random.randint(1, 20000) for _ in range(N)]

target = 20000
```

### Timing Results

| Version |      N | Time Taken |
| ------- | -----: | ---------: |
| Naive   |  5,000 | **332 ms** |
| Naive   | 50,000 | **31.8 s** |

### 7. What happened to the time when `N` grew by 10 times? Does this match what you would expect from a nested-loop approach?

The time increased from about **332 ms to 31.8 seconds** when `N` increased by 10 times. This is roughly a 100-times increase, which is consistent with the **O(N²)** complexity of nested loops. Each element is compared with many other elements, so increasing the input size greatly increases the number of comparisons.

---

## Step 2: Hint

For each number `x` in the list, the value you actually need to find is:

```text
target - x
```

Instead of scanning the rest of the list to look for it, use a **hash set** to check whether the required value has already been seen.

A hash set provides approximately **O(1) average-time lookup**.

### Optimized Approach

The optimized solution makes a single pass through the list:

1. Calculate `target - x`.
2. Check whether the complement is already in the set.
3. If it is, increment the pair count.
4. Add `x` to the set.
5. Continue to the next element.

### Timing Result

| Version   |      N | Time Taken |
| --------- | -----: | ---------: |
| Optimized | 50,000 |  **43 ms** |

---

## 8. Compare the Naive and Optimized Times

For `N = 50,000`:

| Approach  | Time Taken |
| --------- | ---------: |
| Naive     | **31.8 s** |
| Optimized |  **43 ms** |

The optimized solution is dramatically faster because it avoids scanning the remaining list for every element.

---

## 9. What category of change made this faster?

This improvement comes from **both a smarter algorithm and a smarter data structure**. The naive approach uses two nested loops, giving **O(N²)** time complexity. The optimized approach uses a single pass and a hash set with approximately **O(1)** average lookup, reducing the overall complexity to approximately **O(N)**.
