import click
from grid_helper import Grid
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    input_table = list()
    with open(file_path) as file:
        for line in file.read().splitlines():
            input_table.append([elem for elem in line])

    rolls = 0
    new_rolls = 0
    grid = Grid(input_table)
    while new_rolls > 0 or rolls == 0:
        new_rolls = 0
        for position in grid.get_positions('@'):
            count = grid.get_neighbor_number(position, '@')
            if count < 4:
                new_rolls += 1
                grid.update_value(position, 'X')
        rolls += new_rolls
    
    print(f"Total rolls: {rolls}")

if __name__ == "__main__":
    main()