import click
import re
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    
    sum_part_1 = 0
    sum_part_2 = 0
    ids_list = data.split(",")
    ids_list = [tuple(map(int, ids.split("-"))) for ids in ids_list]
    for id in ids_list:
        for i in range(id[0], id[1] + 1):
            if re.match(r"^(.+)\1$", str(i)):
                sum_part_1 += i
                sum_part_2 += i
            elif re.match(r"^(.+)\1+$", str(i)):
                sum_part_2 += i

    click.echo(f"Adding up all the invalid IDs for part 1 is {sum_part_1}")
    click.echo(f"Adding up all the invalid IDs for part 2 is {sum_part_2}")

if __name__ == "__main__":
    main()