import os

here = os.path.dirname(os.path.abspath(__file__))

def get_pairs():
    with open(os.path.join(here, "input.txt")) as f:
        data = f.readline().strip().split(',')
    
    pairs = [(j for j in entry.split('-')) for entry in data]

    return pairs

def part_one():
    pairs = get_pairs()
    invalid_id_sum = 0
    
    for i, j in pairs:
        lower_bound = int(i)
        upper_bound = int(j)
        lower_digit_count = int(len(i) // 2)
        upper_digit_count = int(len(j) // 2)
        
        if len(i) == len(j) and len(i) % 2 != 0:
            continue
        elif len(i) != len(j):
            if len(i) % 2 != 0:
                lower_bound = 10 ** (len(i))
                lower_digit_count = int((len(i) + 1) // 2)
            if len(j) % 2 != 0:
                upper_bound = 10 ** (len(j) - 1) - 1
                upper_digit_count = int((len(j) - 1) // 2)
        
        for seq_len in range(lower_digit_count, upper_digit_count + 1):
            factor = (10 ** seq_len + 1)
            current_lower = lower_bound
            current_upper = upper_bound
            if 10 ** (seq_len * 2 - 1) > lower_bound:
                current_lower = 10 ** (seq_len * 2 - 1) 
            if 10 ** (seq_len * 2) - 1 < upper_bound:
                current_upper = 10 ** (seq_len * 2) - 1
            lower_multiple = current_lower // factor
            upper_multiple = current_upper // factor 

            for m in range(lower_multiple, upper_multiple + 1):
                value = m * factor
                if value >= current_lower and value <= current_upper:
                    invalid_id_sum += value

    print(f"Sum of Invalid Gift IDs: {invalid_id_sum}")

def part_two():
    pass

def main():
    part_one()
    
if __name__ == "__main__":
    main()
