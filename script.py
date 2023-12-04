import sys
import os
from collections import Counter

def frequency(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[1:]]
    max = frequency(numbers)
    print(max)
    