import maze
import generate_maze
import solve_maze


def main():
    current_maze = maze.Maze('create')
    generate_maze.create_maze(current_maze)
    solve_maze.solve_maze(current_maze)
    while 1:
        maze.check_for_exit()
    return


main()
