from functools import cache

def split(number):
    numbers = None
    if number == 0:
        numbers = [1]
    else:
        number_s = str(number)
        l = len(number_s)
        if l % 2 == 0:
            numbers = [int(number_s[:l//2]), int(number_s[l//2:])]
        else:
            numbers = [number * 2024]

    return numbers

# input
numbers = list(map(int, input().split()))

@cache
def count_after_blink(num, times):
    new_numbers = split(num)

    if times == 1:
        return len(new_numbers)

    count = 0    
    for new_num in new_numbers:
        count += count_after_blink(new_num, times - 1)

    return count

ans = 0
for num in numbers:
    ans += count_after_blink(num, 75)

print(ans)
