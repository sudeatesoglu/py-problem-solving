# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(text):
    result_text = ""
    for char in text:
        if char.isalpha():

            if char.isupper():
                result_text += char.lower()

            elif char.islower():
                result_text += char.upper()

        else:
            result_text += char

    return result_text


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
OR;
def swap_case(s):
    result_text = "".join(map(lambda x:x.lower() if x.isupper() else x.upper(), s))
    return result_text
'''
