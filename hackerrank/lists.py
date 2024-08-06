# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    arr = []

    for i in range(N):
        command = input().split()
        request = command[0]

        if request == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif request == "print":
            print(arr)
        elif request == "remove":
            arr.remove(int(command[1]))
        elif request == "append":
            arr.append(int(command[1]))
        elif request == "sort":
            arr.sort()
        elif request == "pop":
            arr.pop()
        elif request == "reverse":
            arr.reverse()
