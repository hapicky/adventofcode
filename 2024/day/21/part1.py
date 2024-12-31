from sys import stdin
from itertools import permutations, product

num_key_points = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
}

dir_key_points = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

direction = {
    '^': (0, -1),
    '<': (-1, 0),
    'v': (0, 1),
    '>': (1, 0)
}

def point_path_to_dir_key_options(path, ng_point):
    dir_key_options = set([''])

    for i in range(len(path) - 1):
        fp = path[i]
        tp = path[i+1]

        dx = tp[0] - fp[0]
        dy = tp[1] - fp[1]

        dir_key = ''
        for _ in range(abs(dx)):
            if dx > 0:
                dir_key += '>'
            else:
                dir_key += '<'

        for _ in range(abs(dy)):
            if dy > 0:
                dir_key += 'v'
            else:
                dir_key += '^'
        
        dir_key_option = set()
        for order in permutations(range(len(dir_key))):
            x = fp[0]
            y = fp[1]

            ng = False
            option = ''
            for j in range(len(dir_key)):
                o = order.index(j)
                px, py = direction[dir_key[o]]
                option += dir_key[o]
                nx = x + px
                ny = y + py

                if nx == ng_point[0] and ny == ng_point[1]:
                    ng = True
                    break

                x = nx
                y = ny

            if not ng:
                dir_key_option.add(option)

        new_dir_key_options = set()
        for op1, op2 in product(dir_key_options, dir_key_option):
            option = op1 + op2 + 'A'
            new_dir_key_options.add(option)

        dir_key_options = new_dir_key_options

    return dir_key_options


ans = 0
for line in stdin:
    code = line.rstrip('\n')

    num_path = [num_key_points['A']] + [num_key_points[c] for c in code]

    dir_robo_options = point_path_to_dir_key_options(num_path, (0, 3))

    shortest = None
    for dir_robo_option in dir_robo_options:
        dir_robo_path = [dir_key_points['A']] + [dir_key_points[c] for c in dir_robo_option]

        dir_key_options = point_path_to_dir_key_options(dir_robo_path, (0, 0))
        for dir_key_option in dir_key_options:
            dir_key_path = [dir_key_points['A']] + [dir_key_points[c] for c in dir_key_option]

            seq_options = point_path_to_dir_key_options(dir_key_path, (0, 0))

            for seq_option in seq_options:
                if shortest is None:
                    shortest = seq_option
                elif len(shortest) > len(seq_option):
                    shortest = seq_option

    print(code, shortest)
    complexity = len(shortest) * int(code[:3])
    ans += complexity

print(ans)
