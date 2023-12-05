from sys import stdin
import heapq

# 変換の実行
def do_map(source, mappings):
    if len(mappings) == 0:
        return source

    mappings.sort()
    result = []

    # print('source:', source)
    # print('mappings:', mappings)

    for src in source:
        # print('src:', src)
        q = [src]
        heapq.heapify(q)

        for i, mapping in enumerate(mappings):
            # print('mapping:', mapping)
            s_start, s_end, d_start = mapping

            while len(q) > 0:
                s, e = heapq.heappop(q)

                if e < s_start:
                    # print('A')
                    # source  |---|
                    # mapping       |---|
                    result.append((s, e))
                    # print('result:', result)
                    continue

                if s < s_start and s_start <= e and e <= s_end:
                    # print('B')
                    # source  |---|
                    # mapping   |---|
                    result.append((s, s_start-1))
                    d_s = d_start
                    d_e = d_start + (e - s_start)
                    result.append((d_s, d_e))
                    # print('result:', result)
                    continue

                if s < s_start and s_end < e:
                    # print('C')
                    # source  |-------|
                    # mapping   |---|
                    result.append((s, s_start-1))
                    result.append((d_start, d_start + (s_end - s_start)))
                    # 超えた範囲はキューに追加して次のマッピングと範囲を比較
                    heapq.heappush(q, (s_end+1, e))
                    # print('result:', result)
                    continue

                if s_start <= s and e <= s_end:
                    # print('D')
                    # source    |---|
                    # mapping |-------|
                    d_s = d_start + (s - s_start)
                    d_e = d_start + (e - s_start)
                    result.append((d_s, d_e))
                    # print('result:', result)
                    continue

                if s_start <= s and s <= s_end and s_end < e:
                    # print('E')
                    # source    |---|
                    # mapping |---|
                    result.append((d_start + (s - s_start), d_start + (s_end - s_start)))
                    # 超えた範囲はキューに追加して次のマッピングと範囲を比較
                    heapq.heappush(q, (s_end+1, e))
                    # print('result:', result)
                    continue

                if s_end < s:
                    # print('F')
                    # source        |---|
                    # mapping |---|
                    if i == len(mappings) - 1:
                        result.append((s, e))
                        # print('result:', result)
                    else:
                        # キューに追加して次のマッピングと範囲を比較
                        heapq.heappush(q, (s, e))
                        break

    result.sort()
    # print('result:', result[0])
    # print('---')
    return result


mappings = []
for line in stdin:
    if line.startswith('seeds:'):
        # 最初の値
        seeds = list(map(int, line.split(':')[1].split()))
        source = []
        for i in range(len(seeds) // 2):
            # (start, end) の形で保持
            s = seeds[i*2]
            e = s + seeds[i*2+1] - 1
            source.append((s, e))

        source.sort()
        continue

    if 'map' in line:
        # マッピングの初期化
        mappings = []
        # print(line.rstrip())
        continue

    if line.rstrip() == '':
        # マッピング終わり→変換
        source = do_map(source, mappings)
        continue

    # マッピングルールの追加
    d_start, s_start, length = map(int, line.split())
    # (source start, source end, destination start) の形で保持
    mappings.append((s_start, s_start + length - 1, d_start))

# 最後の変換を実行
source = do_map(source, mappings)

# 答え
ans = source[0][0]
print(ans)
