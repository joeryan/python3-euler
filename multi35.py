#!/usr/bin/env python3
# multiples of 3 and 5 project Euler
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(max_number):
    sum = 0
    for num in range(max_number):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

