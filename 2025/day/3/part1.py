from sys import stdin

def largest_joltage(bank):
    batteries = [bank[-2], bank[-1]]

    for i in range(len(bank) - 3, -1, -1):
        prev_battery = bank[i]

        for j in range(len(batteries)):
            if prev_battery >= batteries[j]:
                tmp_battery = batteries[j]
                batteries[j] = prev_battery
                prev_battery = tmp_battery
            else:
                break

    largest = int(''.join(batteries))
    return largest


def main():
    ans = 0
    for line in stdin:
        ans += largest_joltage(line.rstrip())

    print(ans)


if __name__ == "__main__":
    main()
