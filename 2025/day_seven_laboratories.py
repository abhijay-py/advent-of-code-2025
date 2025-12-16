import os

here = os.path.dirname(os.path.abspath(__file__))
filename = "input_files/d7_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    data_out = [line.strip() for line in data]
    return data_out


def part_one():
    grid = get_data()
    width = len(grid[0])

    beam_positions = [0] * width
    next_beam_positions = [0] * width

    first_beam_position = 0
    last_beam_position = width - 1
    next_first_beam_position = width
    next_last_beam_position = -1

    split_count = 0

    for line in grid:
        for i in range(first_beam_position, last_beam_position + 1):
            if beam_positions[i] == 1:
                    if line[i] == '^':
                        if i != 0:
                            next_beam_positions[i-1] = 1
                            next_last_beam_position = i-1
                            if next_first_beam_position == width:
                                next_first_beam_position = i-1
                        if i != width - 1:
                            next_beam_positions[i+1] = 1
                            next_last_beam_position = i+1
                            if next_first_beam_position == width:
                                next_first_beam_position = i+1
                        split_count += 1
                    else:
                        next_beam_positions[i] = 1
                        next_last_beam_position = i
                        if next_first_beam_position == width:
                                next_first_beam_position = i
            elif line[i] == 'S':
                next_beam_positions[i] = 1
                next_last_beam_position = i
                next_first_beam_position = i
                break

        beam_positions = next_beam_positions
        next_beam_positions = [0] * width
        last_beam_position = next_last_beam_position
        first_beam_position = next_first_beam_position
        next_first_beam_position = width
        
    print("Classical Tachyon Manifold Beam Split Count:", split_count)


def part_two():
    grid = get_data()
    width = len(grid[0])

    beam_positions = [0] * width
    next_beam_positions = [0] * width

    first_beam_position = 0
    last_beam_position = width - 1
    next_first_beam_position = width
    next_last_beam_position = -1

    for line in grid:
        for i in range(first_beam_position, last_beam_position + 1):
            if beam_positions[i] > 0:
                if line[i] == '^':
                    if i != 0:
                        next_beam_positions[i-1] += beam_positions[i]
                        next_last_beam_position = i-1
                        if next_first_beam_position == width:
                            next_first_beam_position = i-1
                    if i != width - 1:
                        next_beam_positions[i+1] += beam_positions[i]
                        next_last_beam_position = i+1
                        if next_first_beam_position == width:
                            next_first_beam_position = i+1
                else:
                    next_beam_positions[i] += beam_positions[i]
                    next_last_beam_position = i
                    if next_first_beam_position == width:
                            next_first_beam_position = i
            elif line[i] == 'S':
                    next_beam_positions[i] = 1
                    next_last_beam_position = i
                    next_first_beam_position = i
                    break
            

        beam_positions = next_beam_positions
        next_beam_positions = [0] * width
        last_beam_position = next_last_beam_position
        first_beam_position = next_first_beam_position
        next_first_beam_position = width

    split_count = sum(beam_positions)
    print("Quantum Tachyon Manifold Beam Timeline Count:", split_count)

def day_seven_solution():
    part_one()
    part_two()
   
def main():
    day_seven_solution()
    
if __name__ == "__main__":
    main()
