import random
from student import students


def generate_programming_pairs():
    random.shuffle(students)
    for i in range(0, len(students), 2):
        print(students[i].slack_handle, end=' & ')
        print(students[i+1].slack_handle)


if __name__ == '__main__':
    generate_programming_pairs()