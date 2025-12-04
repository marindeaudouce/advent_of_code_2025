import click
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
@click.option("--batteries", "-b", default=2, help="Number of batteries", required=True)
def main(file_path, batteries):
    total_joltage = 0
    with open(file_path, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            numbers = [int(x) for x in list(line)]

            index = 0
            joltage = list()
            for battery in range(batteries, 0, -1):
                if battery == 1:
                    # print(f"Battery {battery}, range {numbers[index:]}")
                    number = max(numbers[index:])
                else:
                    window = numbers[index:-battery+1]
                    number = max(window)
                    index += window.index(number) + 1
                    # print(f"Battery {battery}, range {window}, max {number}, new index {index}")
                # print(f"Selected number: {number} at index {index}")
                joltage.append(number)
            # print(f"Joltage: {joltage} at line {line}")
            total_joltage += int("".join(map(str, joltage)))
    click.echo(f"Total joltage: {total_joltage}")

if __name__ == "__main__":
    main()