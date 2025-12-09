import click
from itertools import combinations
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    # Read the input file
    with open(file_path) as file:
        content = file.read()

    positions = list()
    for line in content.splitlines():
        positions.append([int(pos) for pos in line.split(',')])
    
    areas = list()
    combinations_of_positions = combinations(positions, 2)
    for combo in combinations_of_positions:
        (x1, y1), (x2, y2) = combo
        areas.append((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))
    print(f"Max area part 1: {max(areas)}")

if __name__ == "__main__":
    main()