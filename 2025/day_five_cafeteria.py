import os

here = os.path.dirname(os.path.abspath(__file__))
filename = "input_files/d5_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        ranges = []
        values = []
        line = f.readline()
        reading_values = False
        while line != '':
            if reading_values:
                reading_values = True
                values.append(int(line.strip()))
            elif line == '\n':
                reading_values = True
            else:
                range = line.strip().split('-')
                ranges.append((int(range[0]), int(range[1])))
            line = f.readline()
    return ranges, values


def part_one():
    ranges, values = get_data()
    ranges.sort(key=lambda x: x[0])
    values.sort()

    current_range_idx = 0
    finished_counting = False
    fresh_ingredient_count = 0

    for i in values:
        while i > ranges[current_range_idx][1]:
            current_range_idx += 1
            if current_range_idx >= len(ranges):
                finished_counting = True
                break
        if finished_counting:
            break
        if i >= ranges[current_range_idx][0]:
            fresh_ingredient_count += 1

    print(f"Fresh Ingredients Count: {fresh_ingredient_count}")

def part_two():
    ranges, values = get_data()
    ranges.sort(key=lambda x: x[0])
    
    fresh_ingredient_count = 0
    current_range = [-1, -1]

    for low, high in ranges:
        if low >= current_range[0] and low <= current_range[1]:
            if high > current_range[1]:
                current_range[1] = high
        else:
            if current_range[0] != -1:
                fresh_ingredient_count += current_range[1] - current_range[0] + 1
            current_range = [low, high]
        
    fresh_ingredient_count += current_range[1] - current_range[0] + 1

    print(f"Total Count of Possible Fresh Ingredients: {fresh_ingredient_count}")

def day_five_solution():
    part_one()
    part_two()
   
def main():
    day_five_solution()
    
if __name__ == "__main__":
    main()
