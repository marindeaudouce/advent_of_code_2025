import click
    
@click.command()
@click.option("--file_path", "-f", default="./", help="Path to input file", required=True)
def main(file_path):
    def repeated_times(number: int, times: int) -> bool:
        str_num = str(number)
        len_num = len(str_num)
        if len_num % times != 0:
            return False
        chunk = len_num // times
        first = str_num[:chunk]
        for k in range(1, times):
            if str_num[k * chunk:(k + 1) * chunk] != first:
                return False
        return True

    sum_part_1 = sum_part_2 = 0
    with open(file_path, "r") as file:
        data = file.read()
        ids_list = data.split(",")
        ids_list = [tuple(map(int, ids.split("-"))) for ids in ids_list]
        for id in ids_list:
            for i in range(id[0], id[1] + 1):
                if repeated_times(i, 2):
                    sum_part_1 += i
                    sum_part_2 += i
                elif repeated_times(i, 3) or repeated_times(i, 5) or repeated_times(i, 7):
                    sum_part_2 += i

    click.echo(f"Adding up all the invalid IDs for part 1 is {sum_part_1}")
    click.echo(f"Adding up all the invalid IDs for part 2 is {sum_part_2}")

if __name__ == "__main__":
    main()