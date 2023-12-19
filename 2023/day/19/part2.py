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


negate_op = {
    '<': '>',
    '>': '<',
}

def traverse(wf, conditions):
    next_conditions = tuple(list(conditions))
    wf_conditions = workflows[wf]

    for cond in wf_conditions:
        if cond == 'R':
            return
        
        if cond == 'A':
            accepted_conditions.append(next_conditions)
            return

        if ':' not in cond:
            q.append((cond, next_conditions))
            return

        left, right = cond.split(':')
        k = left[0]
        op = left[1]
        v = int(left[2:])
        new_cond = (k, op, v)
        new_conditions = tuple(list(next_conditions) + [new_cond])



        if right == 'A':
            accepted_conditions.append(new_conditions)
        elif right == 'R':
            # 何もしないでいい？
            None
        else:
            q.append((right, new_conditions))
        
        neg_cond = (k, negate_op[op], v)
        next_conditions = tuple(list(next_conditions) + [neg_cond])


q = []
wf = 'in'
conditions = ()
q.append((wf, conditions))
accepted_conditions = []

while q:
    wf, conditions = q.pop(0)
    traverse(wf, conditions)

ans = 0

ok_conditions = []

for conditions in accepted_conditions:
    min_x = min_m = min_a = min_s = 1
    max_x = max_m = max_a = max_s = 4000
    # print(conditions)

    for k, op, v in conditions:
        if k == 'x':
            if op == '<':
                max_x = min(max_x, v-1)
            else:
                min_x = max(min_x, v+1)
        elif k == 'm':
            if op == '<':
                max_m = min(max_m, v-1)
            else:
                min_m = max(min_m, v+1)
        elif k == 'a':
            if op == '<':
                max_a = min(max_a, v-1)
            else:
                min_a = max(min_a, v+1)
        else:
            if op == '<':
                max_s = min(max_s, v-1)
            else:
                min_s = max(min_s, v+1)
    
    # print(min_x, max_x, min_m, max_m, min_a, max_a, min_s, max_s)

    if max_x < min_x or max_m < min_m or max_a < min_a or max_s < min_s:
        # print('reject')
        continue

    ok_conditions.append((min_x, max_x, min_m, max_m, min_a, max_a, min_s, max_s))
    # print('ok')
    ans += (max_x - min_x + 1) * (max_m - min_m + 1) * (max_a - min_a + 1) * (max_s - min_s + 1)

# サンプルで数が合わない。重複をカウントしてしまっているだろうか？
print(ans)

# print('---')

# for cond in sorted(ok_conditions):
#     print(cond)
