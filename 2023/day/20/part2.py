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
    if output == 'rx':
        rx_received[pulse] += 1

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

import sys
TIMES = sys.maxsize
# TIMES = 100000000
q = []
conjunction_memory = defaultdict(dict)

for t in range(1, TIMES+1):
    q.append(('button', 'broadcaster', 'low'))
    rx_received = defaultdict(int)

    while len(q) > 0:
        buffer = q.copy()
        q.clear()

        for input, output, pulse in buffer:
            send(input, output, pulse)

    if list(rx_received.items()) == [('low', 1)]:
        print(t)
        exit()

    if t % 1000000 == 0:
        print('now: ', t)

    # print('---')

print('not enough.')
exit(1)
