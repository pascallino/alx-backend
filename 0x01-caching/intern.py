#!/usr/bin/python3
import sys

print("I")

# Counting the number of int objects before line 2
with open("file.py", "w") as f:
    # Counting the number of small positive and negative int objects
    num_small_posints = sys.getsizeof(range(sys.maxsize)) // sys.getsizeof(1)
    num_small_negints = sys.getsizeof(range(-sys.maxsize - 1, 0)) // sys.getsizeof(-1)
    total_small_ints = num_small_posints + num_small_negints

    f.write(str(total_small_ints))