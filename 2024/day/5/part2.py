from sys import stdin
from collections import defaultdict

after_pages = defaultdict(set)
before_pages = defaultdict(set)

# input rules
for line in stdin:
    line = line.rstrip('\n')
    if line == '':
        break

    X, Y = map(int, line.split('|'))
    after_pages[X].add(Y)
    before_pages[Y].add(X)

def is_after(cur, after):
    if after in after_pages[cur]:
        return True

    return False

def is_before(cur, before):
    if before in before_pages[cur]:
        return True

    return False

def correct_order(pages):
    corrected = pages.copy()

    for i in range(len(corrected) - 1):
        for j in range(i+1, len(corrected)):
            if is_before(corrected[i], corrected[j]) or is_after(corrected[j], corrected[i]):
                tmp = corrected[i]
                corrected[i] = corrected[j]
                corrected[j] = tmp
    
    return corrected

ans = 0

# input updates
for line in stdin:
    pages = list(map(int, line.rstrip('\n').split(',')))

    valid = True
    for i in range(len(pages) - 1):
        for j in range(i+1, len(pages)):
            if is_before(pages[i], pages[j]):
                valid = False
                break

            if is_after(pages[j], pages[i]):
                valid = False
                break
    
    if not valid:
        corrected = correct_order(pages)
        ans += corrected[len(corrected) // 2]

print(ans)
