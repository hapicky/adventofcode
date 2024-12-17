# input
A = int(input().split()[2])
B = int(input().split()[2])
C = int(input().split()[2])

input()
program = list(map(int, input().split()[1].split(',')))


def operand_value(operand):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        return operand

def division(a, operand):
    denominator = pow(2, operand_value(operand))
    return a // denominator

# run the program
position = 0
outputs = []

while position < len(program) - 1:
    opcode = program[position]
    operand = program[position+1]

    if opcode == 0:
        # adv
        A = division(A, operand)
    elif opcode == 1:
        # bxl
        result = B ^ operand
        B = result
    elif opcode == 2:
        # bst
        result = operand_value(operand) % 8
        B = result
    elif opcode == 3:
        # jnz
        if A != 0:
            position = operand
            continue
    elif opcode == 4:
        # bxc
        result = B ^ C
        B = result
    elif opcode == 5:
        # out
        result = operand_value(operand) % 8
        outputs.append(result)
    elif opcode == 6:
        # bdv
        B = division(A, operand)
    elif opcode == 7:
        # cdv
        C = division(A, operand)

    position += 2


ans = ','.join(map(str, outputs))
print(ans)
