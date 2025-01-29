import time
import random

start_time = time.time()
with open('C:/Users/Artem/Desktop/input.txt') as input_file, open('C:/Users/Artem/Desktop/output.txt', 'w') as output_file:
    output_file.write(str(sum(set([int(x) for x in input_file.read().split("\n")[:-1]]))))
end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")
'''

with open('C:/Users/Artem/Desktop/input.txt', 'w') as input_file:
    for i in range(1000):
        input_file.write(str(int(random.random() * 2.0e+31)) + "\n")
'''