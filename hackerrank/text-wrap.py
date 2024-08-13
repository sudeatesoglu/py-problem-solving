# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap


def wrap(text, width):
    wrapped_string = textwrap.fill(text, width=width)
    return wrapped_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


'''
OR;
def wrap(text, width):
    wrapped_string = ""
    for i in range(0, len(text), width):
        wrapped_string += text[i:i+width] + '\n'
    return wrapped_string
'''
