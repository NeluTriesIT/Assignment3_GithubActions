import sys
from collections import Counter


def frequency(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[1:]]
    max = frequency(numbers)
<<<<<<< HEAD
    print(max)
=======
    print(max)
>>>>>>> 4a0f185 (script changes)
