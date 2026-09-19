import time
start = time.time()

n = 2000000

# Sieve
is_prime = [True] * n
is_prime[0] = is_prime[1] = False

for p in range(2,n//2+1):
    if is_prime[p]:
        for multiple in range(p * p, n, p):
            is_prime[multiple] = False

Sum = 0

for i in range(2, n):
    if is_prime[i]:
        Sum += i

print("Sum of prime numbers:", Sum)
print("Time taken:", time.time() - start)