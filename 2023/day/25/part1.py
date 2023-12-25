from sys import stdin
from collections import defaultdict
from itertools import combinations

# コンポーネント間の接続状況
routes = defaultdict(set)
route_keys = list()
components = set()

# 入力
for line in stdin:
    left, right = line.rstrip().split(': ')

    for r in right.split(' '):
        comp1, comp2 = sorted([left, r])
        routes[comp1].add(comp2)
        routes[comp2].add(comp1)
        route_keys.append((comp1, comp2))
        components.add(comp1)
        components.add(comp2)


# 探索
def visit(cmp, grp, component_group, disconnected_route_keys, q):
    component_group[cmp] = grp

    for next_cmp in routes[cmp]:
        if next_cmp in component_group:
            continue

        if tuple(sorted([cmp, next_cmp])) in disconnected_route_keys:
            continue
        
        q.append((next_cmp, grp))


# 2組になるかどうか探索する
def find_two_groups(disconnected_route_keys):
    component_group = dict()
    group = 1

    for comp in components:
        if comp in component_group:
            continue

        q = []
        q.append((comp, group))

        while len(q) > 0:
            cmp, grp = q.pop(0)
            visit(cmp, grp, component_group, disconnected_route_keys, q)
        
        group += 1
    
    if max(component_group.values()) == 2:
        one = list(component_group.values()).count(1)
        return one * (len(components) - one)
    else:
        return None


# 経路のうち3つを無効にして、2組に分かれるケースを探す
for cmb in combinations(route_keys, 3):
    ans = find_two_groups(cmb)
    if ans is not None:
        print(ans)
        break
