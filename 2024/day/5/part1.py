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

    # 再帰する必要はないらしい
    # for nex in after_pages[cur]:
    #     if is_after(nex, after):
    #         return True
    
    return False

def is_before(cur, before):
    if before in before_pages[cur]:
        return True

    # 再帰する必要はないらしい
    # for nex in before_pages[cur]:
    #     if is_before(nex, before):
    #         return True
    
    return False

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
    
    if valid:
        ans += pages[len(pages) // 2]

print(ans)
