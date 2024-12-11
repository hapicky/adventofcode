numbers = list(map(int, input().split()))

def blink(number, cur_times, until):
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

    if until - cur_times == 1:
        return numbers
    else:
        new_numbers = []
        for num in numbers:
            new_numbers.extend(blink(num, cur_times+1, until))

        return new_numbers


new_numbers = []
for num in numbers:
    new_numbers.extend(blink(num, 0, 25))

ans = len(new_numbers)
print(ans)
