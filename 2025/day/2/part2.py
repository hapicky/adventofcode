def is_invalid_id(id):
    id_str = str(id)
    id_len = len(id_str)

    for digit in range(1, id_len):
        if id_len % digit != 0:
            continue
        
        times = id_len // digit
        if id_str[:digit] * times == id_str:
            return True

    return False


def main():
    ranges = input().split(',')
    ans = 0

    for r in ranges:
        low, high = map(int, r.split('-'))

        for id in range(low, high + 1):
            if is_invalid_id(id):
                ans += id

    print(ans)


if __name__ == "__main__":
    main()
