def next_invalid_id(id):
    id_str = str(id)

    if len(id_str) % 2 == 0:
        id_left = id_str[:len(id_str) // 2]
        invalid_id = int(id_left * 2)

        if invalid_id >= id:
            return invalid_id
        else:
            id_left_incr = str(int(id_left) + 1)
            return int(id_left_incr * 2)
    else:
        id_left = str(10 ** (len(id_str) // 2))
        return int(id_left * 2)


def main():
    ranges = input().split(',')
    ans = 0

    for r in ranges:
        low, high = map(int, r.split('-'))

        invalid_id = next_invalid_id(low)
        while invalid_id <= high:
            ans += invalid_id
            invalid_id = next_invalid_id(invalid_id + 1)

    print(ans)


if __name__ == "__main__":
    main()
