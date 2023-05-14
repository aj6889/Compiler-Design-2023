def left_factoring(s):
    substrings = s.split('|')

    prefix = ''
    for i in range(min(map(len, substrings))):
        if len(set(substring[i] for substring in substrings)) == 1:
            prefix += substrings[0][i]
        else:
            break

    if prefix:
        s = prefix + '(' + '|'.join(substring[len(prefix):] for substring in substrings) + ')'
    return s

s = input()
print(left_factoring(s))

'''
Input: 
abab|abac|abc
Output:
ab(ab|ac|c)

'''
