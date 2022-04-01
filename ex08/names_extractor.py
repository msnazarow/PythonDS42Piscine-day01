import sys


def main(*args):
    output_name = "employees.tsv"
    if len(args) != 2:
        return
    with open(args[1]) as input:
        with open(output_name, 'w') as output:
            output.write("Name\tSurname\tEmail\n")
            for line in input:
                name, surname = line.split('@')[0].split('.')
                output.write(f"{name.capitalize()}\t{surname.capitalize()}\t{line}\n")


if __name__ == '__main__':
    main(*sys.argv)
