import pandas

def main():
    variants = pandas.read_csv("~/Desktop/training_variants.txt")
    new_text = pandas.read_csv("~/Desktop/training_text.txt",
                               header=0,
                               sep="\\|\\|",
                               engine="python"
    )
#    with pandas.option_context('display.max_rows', None, 
#                               'display.max_columns', None
#                              ):
#        print(new_text)
#        print(variants)

    print(new_text.shape, variants.shape, sep="\n", end="")
    print(new_text.columns.values, variants.columns.values, sep="\n", end="")
    
if __name__=="__main__":
    main()
