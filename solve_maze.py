import random


BIT_SOLUTION = 0b0000010010010110
# Solve maze using Pre-Order DFS algorithm, terminate with solution


def solve_maze(m):
    stack = []
    current_cell = 0
    visited_cells = 1

    while current_cell != m.total_cells - 1:
        print(current_cell)
        unvisited_neighbors = m.cell_neighbors(current_cell)
        if len(unvisited_neighbors) >= 1:
            # choose random neighbor to be new cell
            new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
            new_cell, compass_index = unvisited_neighbors[new_cell_index]
            # knock down wall between it and current cell using visited_cell
            m.visit_cell(current_cell, new_cell, compass_index)
            # push current cell to stack
            stack.append(current_cell)
            # set current cell to new cell
            current_cell = new_cell
            # add 1 to visited cells
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = stack.pop()

        m.refresh_maze_view()
    m.state = 'idle'
