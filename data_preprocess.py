import pandas

def main():
    new_variants = pandas.read_csv("~/Desktop/training_variants.txt")
    with pandas.option_context('display.max_rows', None, 
                               'display.max_columns', None
                              ):
        print(new_variants)
    
if __name__=="__main__":
    main()
