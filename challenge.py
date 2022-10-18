#!/usr/bin/env python3

# Find the most frequent integer in an array
lst = [1, 2, 2, 4, 5, 2, 7, 5, 9, 3]

def most_freq(lst):
    most_frequent = max(set(lst), key=lst.count)
    return most_frequent

# Reverse a String iteratively and recursively
str = "Hello World"

# Iterative
def iterative_rev(s):
    rev_s = ''

    for c in s:
        rev_s = c + rev_s

    return rev_s

# Recursive
def recursive_rev(s):
    
    if len(s) == 0:
        return s
    
    else:
        return recursive_rev(s[1:]) + s[0]

if __name__ == '__main__':
    print(most_freq(lst))
    print(iterative_rev(str))
    print(recursive_rev(str))
