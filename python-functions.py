# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  int = 0
  for n in range(1, n + 1):
    int += n
  return int

print(sum_to(6))