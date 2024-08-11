# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
if __name__ == '__main__':
    s = input()
    x = y = z = t = v = False
    for char in s:
        if char.isalnum():
            x = True
        if char.isalpha():
            y = True
        if char.isdigit():
            z = True
        if char.islower():
            t = True
        if char.isupper():
            v = True

    true_list = [x, y, z, t, v]
    for i in true_list:
        print(i)

'''
OR;
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
'''
