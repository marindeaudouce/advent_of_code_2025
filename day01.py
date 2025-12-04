import click
import operator
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    dial_size = 100
    pointer = 50
    operations_map = {'+': operator.add, '-': operator.sub}
    zeros_counter = goes_around_counter = 0

    with open(file_path, "r") as file:
        for line in file:
            number = int(line[1:])
            operation = operations_map['+' if line.startswith('R') else '-']

            for _ in range(number):
                pointer = operation(pointer, 1) % dial_size
                if pointer == 0:
                    goes_around_counter += 1

            if pointer == 0:
                zeros_counter += 1

    click.echo(f"Number of times pointer landed on zero: {zeros_counter}")     
    click.echo(f"Number of times pointer goes to zero: {goes_around_counter}")


if __name__ == "__main__":
    main()