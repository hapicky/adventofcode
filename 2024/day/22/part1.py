from sys import stdin

def mix(value, sec_number):
    return value ^ sec_number

def prune(sec_number):
    return sec_number % 16777216

ans = 0

for line in stdin:
    sec_number = int(line.rstrip('\n'))

    for _ in range(2000):
        # operation#1
        value = sec_number * 64
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

        # operation#2
        value = sec_number // 32
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

        # operation#3
        value = sec_number * 2048
        sec_number = mix(value, sec_number)
        sec_number = prune(sec_number)

    ans += sec_number

print(ans)
