#!/usr/bin/env python3

def print_fibonacci(length):
    if length < 0:
        print("Input should be a non-negative integer")
        return

    fibonacci_seq = []

    if length > 0:
        fibonacci_seq.append(0)
    if length > 1:
        fibonacci_seq.append(1)

    for i in range(2, length):
        next_value = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_value)

    print(fibonacci_seq)
    pass
