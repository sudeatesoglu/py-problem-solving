# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum_list = []

    for i in range(min(n + 1, 2)):
        maximum = arr[0]
        for i in range(n):
            if arr[i] > maximum:
                maximum = arr[i]
        maximum_list.append(maximum)
        arr = [i for i in arr if i != maximum]
        n = len(arr)

    second_maximum = maximum_list[1]
    print(second_maximum)
