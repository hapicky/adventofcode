from sys import stdin

# 変換の実行
def do_map(source, mappings):
    if len(mappings) == 0:
        return source

    # source range start順にソート
    mappings.sort()
    # sourceと同じ値がデフォルト
    result = source.copy()
    for i, s in enumerate(source):
        for s_start, d_start, length in mappings:
            if s < s_start:
                # source range startより小さい値ならそのまま
                break

            if s_start <= s and s < s_start + length:
                # 範囲内であれば値を変換
                result[i] = d_start + (s - s_start)
                break

    return result


mappings = []
for line in stdin:
    if line.startswith('seeds:'):
        # 最初の値
        source = list(map(int, line.split(':')[1].split()))
        continue

    if 'map' in line:
        # マッピングの初期化
        mappings = []
        continue

    if line.rstrip() == '':
        # マッピング終わり→変換
        source = do_map(source, mappings)
        continue

    # マッピングルールの追加
    d_start, s_start, length = map(int, line.split())
    # source順にソートしたいのでsource range startを先頭にしたtupleとして保持
    mappings.append((s_start, d_start, length))

# 最後の変換を実行
source = do_map(source, mappings)

# 答え
ans = min(source)
print(ans)
