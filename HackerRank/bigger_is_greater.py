#!/usr/bin/env python3
""" Bigger is Greater

HackerRank challenge.
url: https://www.hackerrank.com/challenges/bigger-is-greater
"""

for _ in range(int(input().strip())):
    word = input().strip()

    # Find the "least significant" pattern disruption
    found = False
    for i in range(len(word) - 1, 0, -1):
        if word[i - 1] < word[i]:
            n = i
            found = True
            break
    
    if not found:
        print('no answer')
        continue

    # Letter at position (n - 1) is the "change position"
    # Everything up to (n - 1) is unchanged, Everything after is sorted asc with repl.
    n -= 1

    # The remainder of the string is to be sorted in ascending order.
    # The "disruption" is moved into the correct ascending order, and the letter in that
    #   position is replaced with the lexicographically next highest letter
    rem = sorted(word[n:])
    pos = rem.index(word[n])
    let = [rem[i] for i in range(pos, len(rem)) if rem[i] != word[n]][0]
    del rem[rem.index(let)]

    print(word[:n] + let + ''.join(rem)) 

