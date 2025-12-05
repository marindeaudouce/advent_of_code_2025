import click
import re
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    with open(file_path) as file:
        content = file.read()

    content = content.split("\n\n")
    fresh_ranges = list()
    for line in content[0].splitlines():
        match = re.search(r"^[0-9]+\-[0-9]+$", line)
        if match:
            fresh_ranges.append([int(x) for x in match.group(0).split('-')])

    fresh_counter = 0
    for ingredient in content[1].splitlines():
        for fresh in fresh_ranges:
            start, end = fresh
            if int(ingredient) >= start and int(ingredient) <= end:
                fresh_counter += 1
                break
    print(f"Part1: Fresh ingredients count: {fresh_counter}")

    fresh_ranges.sort(key=lambda tup: tup[0])
    ids_counter = 0
    max_seen = 0
    for fresh in fresh_ranges:
        if fresh[0] > max_seen:
            # print("no overlap")
            ids_counter += fresh[1] - fresh[0] + 1
            max_seen = fresh[1]
        elif fresh[1] > max_seen:
            # print(f"high overlap of {max_seen} and {fresh[1]}")
            ids_counter += fresh[1] - max_seen
            max_seen = fresh[1]   
    print(f"Part2: Number of ids = {ids_counter}")

if __name__ == "__main__":
    main()