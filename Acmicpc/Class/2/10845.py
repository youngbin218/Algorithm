import sys

class Queue():
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        print('-1') if not self.q else print(self.q.pop(0))

    def size(self):
        print(len(self.q))

    def empty(self):
        print('1') if not self.q else print('0')

    def front(self):
        print('-1') if not self.q else print(self.q[0])

    def back(self):
        print('-1') if not self.q else print(self.q[-1])

input = sys.stdin.readline

N = int(input())

q = Queue()

for _ in range(N):
    inst = input().rstrip()
    if inst[:4] == 'push':
        q.push(int(inst[5:]))
    if inst == 'pop':
        q.pop()
    if inst == 'size':
        q.size()
    if inst == 'empty':
        q.empty()
    if inst == 'front':
        q.front()
    if inst == 'back':
        q.back()
