import os

# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])


print(total_memory)
print(used_memory)
print(free_memory)
