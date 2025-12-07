import click
import numpy
from grid_helper import Grid
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    # Read the input file
    with open(file_path) as file:
        content = file.read()

    # Parse the grid
    grid_lines = [list(line) for line in content.splitlines() if line]
    grid = Grid(grid_lines)
    bream_position = grid.get_positions('S')[0]
    
    """ Part 1
    splitter_positions = grid.get_positions('^')
    total_split = 0
    for splitter in splitter_positions:
        above_splitter = [s for s in splitter_positions if s[0] < splitter[0]]
        if not above_splitter and bream_position[1] == splitter[1]:
            total_split += 1
        else:
            side_splitter = [s for s in above_splitter if (s[1] + 1 == splitter[1] or s[1] - 1 == splitter[1])]
            directly_above = [s for s in above_splitter if s[1] == splitter[1]]
            if not directly_above and side_splitter:
                total_split += 1
            elif directly_above[-1][0] < side_splitter[-1][0]:
                total_split += 1
    print(f"Total split = {total_split}")
    """

    # Part 2
    # Helped by https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/
    beams = numpy.zeros(grid.grid_size[0], dtype=int)
    beams[bream_position[1]] = 1
    total_split = 0
    for line in grid.grid_map:
        for index, col in enumerate(line):
            if col == '^':
                if beams[index] > 0:
                    total_split += 1
                beams[index + 1] += beams[index]
                beams[index - 1] += beams[index]
                beams[index] = 0
    print(f"Total split = {total_split}")
    print(f"Total timelines = {numpy.sum(beams)}")
  
if __name__ == "__main__":
    main()