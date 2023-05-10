from student import students
import random

def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

random.shuffle(students)
for group in chunk(students, 3):
    print('\t'.join([s.name for s in group]))