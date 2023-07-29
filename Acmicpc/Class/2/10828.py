import sys

class Stack():
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        print('-1') if not self.s else print(self.s.pop(-1))

    def size(self):
        print(len(self.s))

    def empty(self):
        print('1') if not self.s else print('0')

    def top(self):
        print('-1') if not self.s else print(self.s[-1])

input = sys.stdin.readline

N = int(input())

s = Stack()

for _ in range(N):
    inst = input().rstrip()
    if inst[:4] == 'push':
        s.push(int(inst[5:]))
    if inst == 'pop':
        s.pop()
    if inst == 'size':
        s.size()
    if inst == 'empty':
        s.empty()
    if inst == 'top':
        s.top()
