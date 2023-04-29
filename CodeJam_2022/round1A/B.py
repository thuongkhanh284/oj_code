import random
from sys import stdin


class Solution:
    def __init__(self, n):
        self.n = n
        self.A = None

    def print_init(self):
        for i in range(1, self.n + 1):
            print("%d" % i, end=" ", flush=True)
        print("", flush=True)

    def interactive(self):
        self.A = [int(x) for x in stdin.readline().split()]

        print("1", flush=True)


def interactive_solution_wrapper():
    T = int(stdin.readline())
    for t in range(T):
        n = int(stdin.readline())
        s = Solution(n)
        s.print_init()
        s.interactive()


if __name__ == "__main__":
    interactive_solution_wrapper()