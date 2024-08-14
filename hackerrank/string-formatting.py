# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def print_formatted(number):
    width = len(bin(number)) - 2
    print(f"{1:{width}} {1:{width}} {1:{width}} {1:{width}}")
    for i in range(1, number):
        print(f"{i+1:>{width}} {oct(i+1)[2:]:>{width}} {hex(i+1)[2:].upper():>{width}} {bin(i+1)[2:]:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
