def my_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[i-1] + sequence[i-2]
        sequence.append(next_value)
    
    return sequence
n = 10
print(my_fibonacci(n))

# Recursive implementation of Fibonacci sequence

def R_fibonacci(n):
    if n <= 1:
        return n
    else:
        return R_fibonacci(n-1) + R_fibonacci(n-2)
n = 11
print(my_fibonacci(n))