# Kasseus Andrei D. Baleda
# K240947

import time

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

start_time = time.time()
numbers = [0, 1, 5, 7, 10]

for num in numbers:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")

end_time = time.time()
print(f"\nExecution time: {end_time - start_time:.6f} seconds")
