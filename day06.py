import click
import operator
import re
import numpy
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    # Read the input file
    with open(file_path) as file:
        content = file.read()

    # Operator map
    operations_map = {'+': operator.add, '*': operator.mul}
    
    # Parse the content
    numbers_list = list()
    lines = list()
    for line in content.splitlines():
        numbers = re.findall("[0-9]+", line)
        if numbers:
            numbers_list.append(numbers)
            lines.append(list(line))
        else:
            operators = re.findall(r"[\+\*]", line)
    
    def compute_grand_total(numbers_array: list, operators: list) -> int:
        grand_total = 0
        for index, col in enumerate(numbers_array):
            operation = operations_map[operators[index]]
            result = int(col[0])
            for n in col[1:]:
                result = operation(result, int(n))
            grand_total += result
            # print(f"Result of column {index} with operation {operators[index]}: {result}")
        return grand_total
    
    # Part 1
    numbers_array = numpy.array(numbers_list)
    t_numbers_array = numpy.transpose(numbers_array)
    print(f"Grand total of part 1 is : {compute_grand_total(t_numbers_array, operators)}")

    # Part 2
    np_lines = numpy.array(lines)
    np_cols = numpy.transpose(np_lines)

    new_array = list()
    for col in np_cols:
        number = "".join(col)
        if not number.isspace():
            numbers.append(number)
        else:
            new_array.append(numbers)
            numbers = list()
    new_array.append(numbers)
    print(f"Grand total of part 2 is : {compute_grand_total(new_array, operators)}")

if __name__ == "__main__":
    main()