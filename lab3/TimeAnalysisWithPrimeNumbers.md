# Prime Numbers Performance Analysis

## Step 1: Naive Version

Write a program that computes the sum of all prime numbers strictly below `N`, checking every number from `2` up to `N - 1`, and for each one, testing all possible divisors to decide if it is prime.

### Timing Wrapper

```python
import time

start = time.time()

# your code here

print("Time taken:", time.time() - start)
```

### Test Cases

| Input     | Expected Output |
| --------- | --------------: |
| `N = 10`  |            `17` |
| `N = 2`   |             `0` |
| `N = 3`   |             `2` |
| `N = 20`  |            `77` |
| `N = 100` |          `1060` |

### Timing Results

| Input           |            Output |            Time Taken |
| --------------- | ----------------: | --------------------: |
| `N = 50,000`    |      `68,143,852` | `2.550978660583496 s` |
| `N = 2,000,000` | `142,913,828,922` | `44.41602659225464 s` |

### Observation

**What did you observe? Did the time grow the way you expected when `N` grew by about 40 times?**

The execution time increased significantly as `N` increased. This is expected because the naive approach checks every number individually and tests many possible divisors for each number.

---

## Step 2: Hint 1 — Smaller Divisor Bound

When checking whether a number `x` is prime, do you really need to test every divisor up to `x - 1`?

The smallest upper bound that needs to be checked is:

```text
√x
```

### Why?

If `x` is composite, it must have at least one factor less than or equal to `√x`.

Therefore, if no number from `2` through `√x` divides `x`, then `x` is prime.

### Timing Result

For:

```text
N = 2,000,000
```

The execution time was:

```text
20.46193552017 s
```

### Observation

This version was approximately **2 times faster**, but it was still slow for large values of `N`.

---

## Step 3: Hint 2 — Sieve of Eratosthenes

The current approach solves:

> "Is this number prime?"

separately, from scratch, for every number.

Instead, we can determine which numbers up to `N` are prime **all at once** using the **Sieve of Eratosthenes**.

### Core Idea

The sieve works by eliminating the multiples of a prime number from the range. This reduces the number of candidates that need to be checked and significantly reduces the execution time.

For example, after identifying `2` as prime, we can eliminate:

```text
4, 6, 8, 10, 12, ...
```

Then we move to the next remaining number, `3`, and eliminate its multiples:

```text
6, 9, 12, 15, ...
```

The remaining unmarked numbers are prime.

### Sieve Timing

For:

```text
N = 2,000,000
```

The measured execution time was approximately:

```text
52 ms
```

---

## 5. Comparison of All Three Approaches

For `N = 2,000,000`:

| Approach              |              Time Taken |
| --------------------- | ----------------------: |
| Naive                 | **44.41602659225464 s** |
| Smaller Bound (`√x`)  |    **20.46193552017 s** |
| Sieve of Eratosthenes |               **52 ms** |

The difference is substantial:

```text
Naive
  ↓
44.42 seconds

Smaller Bound
  ↓
20.46 seconds

Sieve
  ↓
0.052 seconds
```

---

## 6. Which Single Change Gave the Biggest Jump in Speed?

The biggest improvement came from **eliminating multiples of known prime numbers** using the Sieve of Eratosthenes.

Instead of repeatedly checking whether every number is prime from scratch, the sieve uses information already discovered about smaller prime numbers to eliminate many composite numbers at once.

This dramatically reduces the amount of work and improves the time complexity from repeated primality testing to approximately:

```text
O(N log log N)
```

for the sieve.

### Conclusion

The progression demonstrates how algorithmic improvements can have a much larger impact than small code-level optimizations:

```text
Naive
    ↓
Check fewer divisors
    ↓
Reuse information with a sieve
```

The Sieve of Eratosthenes provides the largest performance improvement because it avoids performing essentially the same primality checks repeatedly.
