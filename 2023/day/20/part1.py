from sys import stdin
from collections import defaultdict

# モジュール
modules = dict()
# 各モジュールの入力の数（Conjunction用）
input_count = defaultdict(int)

# 入力
for line in stdin:
    f, t = line.rstrip().split(' -> ')
    destinations = t.split(', ')

    if f == 'broadcaster':
        name = type = 'broadcaster'
        modules[name] = {
            'type': type,
            'destinations': destinations
        }
    else:
        name = f[1:]
        type = f[0]

        if type == '%':
            modules[name] = {
                'type': type,
                'destinations': destinations,
                'on': False
            }
        else:
            modules[name] = {
                'type': type,
                'destinations': destinations,
            }
    
    # 入力数をカウント
    for dest in destinations:
        input_count[dest] += 1


# 発生したパルスの数
count = {
    'low': 0,
    'high': 0
}


# 送信処理
def send(input, output, pulse):
    # print(input, pulse, output)
    count[pulse] += 1

    if output not in modules:
        return

    type = modules[output]['type']
    destinations = modules[output]['destinations']

    if type == 'broadcaster':
        for dest in destinations:
            q.append((output, dest, pulse))
    elif type == '%':
        # Flip-flop
        if pulse == 'low':
            if modules[output]['on']:
                next_pulse = 'low'
            else:
                next_pulse = 'high'

            for dest in destinations:
                q.append((output, dest, next_pulse))
            
            modules[output]['on'] = not modules[output]['on']

    elif type == '&':
        # Conjunction
        conjunction_memory[output][input] = pulse

        if list(conjunction_memory[output].values()) == ['high'] * input_count[output]:
            next_pulse = 'low'
        else:
            next_pulse = 'high'
        
        for dest in destinations:
            q.append((output, dest, next_pulse))


TIMES = 1000
q = []
conjunction_memory = defaultdict(dict)

for _ in range(TIMES):
    q.append(('button', 'broadcaster', 'low'))

    while len(q) > 0:
        buffer = q.copy()
        q.clear()

        for input, output, pulse in buffer:
            send(input, output, pulse)

    # print('---')

ans = count['low'] * count['high']
print(ans)
