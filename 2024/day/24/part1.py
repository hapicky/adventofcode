from sys import stdin
from collections import deque

# inputs
inputs = dict()

for line in stdin:
    line = line.rstrip('\n')
    if line == '':
        break

    name, value = line.split(': ')
    inputs[name] = int(value)

# input gates
q = deque()

for line in stdin:
    line = line.rstrip('\n')

    input1, op, input2, _, output = line.split(' ')
    q.append((input1, op, input2, output))

# produce number
ans = 0

while len(q) > 0:
    input1, op, input2, output = q.popleft()

    if input1 in inputs and input2 in inputs:
        # both inputs are ready
        if op == 'AND':
            result = inputs[input1] & inputs[input2]
        elif op == 'OR':
            result = inputs[input1] | inputs[input2]
        else:
            result = inputs[input1] ^ inputs[input2]
        
        if output[0] == 'z':
            if result == 1:
                ans += pow(2, int(output[1:]))
        else:
            inputs[output] = result
    
    else:
        # queue again
        q.append((input1, op, input2, output))

print(ans)
