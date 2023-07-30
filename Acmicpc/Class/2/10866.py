import sys

class Deque():
    def __init__(self):
        self.d = []

    def push_front(self, x):
        self.d.insert(0, x)

    def push_back(self, x):
        self.d.append(x)

    def pop_front(self):
        print('-1') if not self.d else print(self.d.pop(0))

    def pop_back(self):
        print('-1') if not self.d else print(self.d.pop(-1))

    def size(self):
        print(len(self.d))

    def empty(self):
        print('1') if not self.d else print('0')

    def front(self):
        print('-1') if not self.d else print(self.d[0])

    def back(self):
        print('-1') if not self.d else print(self.d[-1])

input = sys.stdin.readline

N = int(input())

s = Deque()

for _ in range(N):
    inst = input().rstrip()
    if inst[:10] == 'push_front':
        s.push_front(int(inst[11:]))
    if inst[:9] == 'push_back':
        s.push_back(int(inst[10:]))
    if inst == 'pop_front':
        s.pop_front()
    if inst == 'pop_back':
        s.pop_back()
    if inst == 'size':
        s.size()
    if inst == 'empty':
        s.empty()
    if inst == 'front':
        s.front()
    if inst == 'back':
        s.back()
