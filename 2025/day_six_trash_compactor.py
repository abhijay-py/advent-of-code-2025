import os

here = os.path.dirname(os.path.abspath(__file__))
filename = "input_files/d6_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        operands = []
        operators = []
        line = f.readline()
        while line != '':
            if '+' in line or '*' in line:
                operators = line
            else:
                operands.append(line)
            line = f.readline()
        
    return operands, operators


def part_one():
    operands, operators = get_data()
    result = 0
    operands = [i.split() for i in operands]
    operators = operators.split()

    for i in range(len(operators)):
        if operators[i] == '+':
            for j in range(len(operands)):
                result += int(operands[j][i])
        else:
            multiplication_result = 1
            for j in range(len(operands)):
                multiplication_result *= int(operands[j][i])
            result += multiplication_result

    print(f"Homework Result: {result}")


def part_two():
    operands, operators = get_data()
    result = 0
    current_operator = ''

    for i in range(len(operators)):
        if operators[i] == '+' or operators[i] == '*':
            current_result = 0 if operators[i] == '+' else 1

            if operators[i] == '+':
                current_operator = lambda x, y: x + y
            else:
                current_operator = lambda x, y: x * y

        operand = 0
        blank = True
        for j in range(len(operands)):
            if operands[j][i] != ' ':
                blank = False
                operand *= 10
                operand += int(operands[j][i])

        if blank:
            result += current_result
            continue

        current_result = current_operator(current_result, operand)
    result += current_result
    print(f"Corrected Homework Result: {result}")

def day_six_solution():
    part_one()
    part_two()
   
def main():
    day_six_solution()
    
if __name__ == "__main__":
    main()
