import pandas

def csv_decoder(filename):

    """
    csv_decoder docstring text
    """

    output_list = []
    with open(filename,"r") as file:
        for line in file:
            output_list.append(line.rstrip("\n").split(","))
    return output_list

def main():
#    variants = csv_decoder("training_variants.txt")
#    for row in variants:
#        print(row)
    new_variants = pandas.read_csv("./training_variants.txt")
    with pandas.option_context('display.max_rows', None, 'display.max_columns', 5):
        print(new_variants)
    
if __name__=="__main__":
    main()
