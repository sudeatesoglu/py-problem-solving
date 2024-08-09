# https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
def straight_pyramid(n):
    for i in range(n):
        width = 2 * n - 1
        pattern = ('H' * (2 * i + 1)).center(width, ' ')
        print(pattern)


def reverse_pyramid(n):
    for i in range(n):
        width = 2 * n - 1
        pattern = (' ' * (4 * n)) + ('H' * (2 * (n - i) - 1)).center(width, ' ')
        print(pattern)


def rectangle(n):
    for i in range((n + 1) // 2):
        pattern = ('H' * 5 * n).center(6 * n - 1, ' ')
        print(pattern)


def square(n):
    for i in range(n + 1):
        pattern = (('H' * n) + (' ' * n * 3) + ('H' * n)).center(n * 6, ' ')
        print(pattern)


N = int(input())
if N % 2 != 0:
    straight_pyramid(N)
    square(N)
    rectangle(N)
    square(N)
    reverse_pyramid(N)
else:
    warning = "n should be a odd integer!"
    print(warning)
