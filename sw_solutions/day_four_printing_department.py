import os
from collections import deque

here = os.path.dirname(os.path.abspath(__file__))
filename = "d4_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    
    data_grid = [list(entry.strip()) for entry in data]

    return data_grid

def part_one():
    data_grid = get_data()
    row_count = len(data_grid)
    col_count = len(data_grid[0])
    accessible_paper_count = 0

    neighbor_count = [0 for i in range(row_count * col_count)]

    for row in range(row_count):
        for col in range(col_count):
            if data_grid[row][col] == '@':
                idx = row * col_count + col
                # check all unexplored directions 
                if (col < col_count - 1 and data_grid[row][col + 1] == '@'): # check E
                    neighbor_count[idx] += 1
                    neighbor_count[idx + 1] += 1
                if (row < row_count - 1):
                    if (col > 0 and data_grid[row + 1][col - 1] == '@'): #check SW
                        neighbor_count[idx] += 1
                        neighbor_count[idx + col_count - 1] += 1
                    if (data_grid[row + 1][col] == '@'): #check S
                        neighbor_count[idx] += 1
                        neighbor_count[idx + col_count] += 1
                    if (col < col_count - 1 and data_grid[row + 1][col + 1] == '@'): #check SE
                        neighbor_count[idx] += 1
                        neighbor_count[idx + col_count + 1] += 1
                
                #check surrounding position count
                if (neighbor_count[idx] < 4):
                    accessible_paper_count += 1

    print(f"First Run Accessible Paper Count: {accessible_paper_count}")

def part_two():
    data_grid = get_data()
    row_count = len(data_grid)
    col_count = len(data_grid[0])
    accessible_paper_count = 0

    edges = {i : [] for i in range(row_count * col_count)}

    for row in range(row_count):
        for col in range(col_count):
            idx = row * col_count + col
            if data_grid[row][col] == '@':
                new_edges = []
                # check all unexplored directions 
                if (col < col_count - 1 and data_grid[row][col + 1] == '@'): # check E
                    new_edges.append(idx + 1)
                if (row < row_count - 1):
                    if (col > 0 and data_grid[row + 1][col - 1] == '@'): #check SW
                        new_edges.append(idx + col_count - 1)
                    if (data_grid[row + 1][col] == '@'): #check S
                        new_edges.append(idx + col_count)
                    if (col < col_count - 1 and data_grid[row + 1][col + 1] == '@'): #check SE
                        new_edges.append(idx + col_count + 1)
                
                #check surrounding position count and update edges
                if (len(new_edges) + len(edges[idx]) < 4):
                    accessible_paper_count += 1
                    data_grid[row][col] = '.'
                    for edge in edges[idx]:
                        edges[edge].remove(idx)
                    del edges[idx]
                else:
                    edges[idx].extend(new_edges)
                    for edge in new_edges:
                        edges[edge].append(idx)
            else:
                del edges[idx]

    check_edges = deque(list(edges.keys()))

    while len(check_edges) > 0:
        idx = check_edges.popleft()

        if len(edges[idx]) < 4:
            accessible_paper_count += 1
            data_grid[int(idx // col_count)][idx % col_count] = '.'
            for edge in edges[idx]:
                edges[edge].remove(idx)
                if edge not in check_edges:
                    check_edges.append(edge)
            del edges[idx]
    
    print(f"Total Accessible Paper Count: {accessible_paper_count}")          

def day_four_solution():
    part_one()
    part_two()
   
def main():
    day_four_solution()
    
if __name__ == "__main__":
    main()
