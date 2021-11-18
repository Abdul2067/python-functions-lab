# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  int = 0
  for n in range(1, n + 1):
    int += n
  return int

print(sum_to(6))



# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([4, 46, 56, 454, 45, 86, 76]))


# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(str1, str2):
  return str1.count(str2)
print(occurances("waves", "e"))


