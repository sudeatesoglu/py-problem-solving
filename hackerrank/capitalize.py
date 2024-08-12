# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
import os


def solve(s):
    text_characters = s.split(" ")
    capitalized_array = []
    for char in text_characters:
        capitalized_char = char.capitalize()
        capitalized_array.append(capitalized_char)

    capitalized_text = " ".join(capitalized_array)

    return capitalized_text


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

'''
OR;
def solve(s):
    capitalized_text = ""
    capitalize_next = True

    for char in s:
        if char == ' ':
            capitalize_next = True
            capitalized_text += char
        elif capitalize_next:
            capitalized_text += char.upper()
            capitalize_next = False
        else:
            capitalized_text += char

    return capitalized_text
    
OR;
def solve(s):
    capitalized_text = s.title()
    return capitalized_text
'''
