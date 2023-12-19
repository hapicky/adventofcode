from sys import stdin

# ワークフローの入力
workflows = dict()
for l in stdin:
    line = l.rstrip()
    if line == '':
        break
    
    name = line.split('{')[0]
    conditions = line[len(name)+1:len(line)-1].split(',')

    workflows[name] = conditions

# パーツの入力
parts = []
for l in stdin:
    line = l.rstrip()
    p = dict()
    for part in line[1:len(line)-1].split(','):
        k, v = part.split('=')
        p[k] = int(v)
    
    parts.append(p)

# レーティングの計算
ans = 0
for p in parts:
    wf = 'in'
    accepted = None

    while accepted is None:
        conditions = workflows[wf]
        for cond in conditions:
            if cond == 'R':
                accepted = False
                break

            if cond == 'A':
                accepted = True
                break

            if ':' not in cond:
                wf = cond
                break
            
            left, right = cond.split(':')
            k = left[0]
            op = left[1]
            v = int(left[2:])

            if op == '<':
                result = (p[k] < v)
            else:
                result = (p[k] > v)
            
            if not result:
                continue

            if right == 'R':
                accepted = False
                break
            elif right == 'A':
                accepted = True
                break
            else:
                wf = right
                break
    
    if accepted:
        ans += sum(p.values())

print(ans)
