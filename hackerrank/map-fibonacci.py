# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x ** 3


def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 0:
        return []

    elif n == 1:
        return [0]

    elif n == 2:
        return [0, 1]

    else:
        fibo = [0, 1]
        for _ in range(2, n):
            fibo_sum = fibo[-1] + fibo[-2]
            fibo.append(fibo_sum)

        return fibo


if __name__ == '__main__':
    N = int(input())
    print(list(map(cube, fibonacci(N))))
