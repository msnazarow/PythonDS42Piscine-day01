if __name__ == "__main__":
    name = "ds.csv"
    with open(name, "r") as input, open(name.replace("csv", "tsv"), 'w') as output:
        for line in input:
            output.write(line.replace(',', '\t'))

