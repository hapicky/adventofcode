from sys import stdin

def largest_joltage(bank):
    batteries = []
    SIZE = 2

    l = 0
    for i in range(SIZE):
        r = len(bank) - SIZE + i
        candidates = bank[l:r+1]

        # take the max digit from the left
        jolt = max(candidates)
        batteries.append(jolt)

        # shift the next start position
        l += candidates.index(jolt) + 1

    largest = int(''.join(batteries))
    return largest


def main():
    ans = 0
    for line in stdin:
        ans += largest_joltage(line.rstrip())

    print(ans)


if __name__ == "__main__":
    main()
