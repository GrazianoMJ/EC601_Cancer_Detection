import pandas

def main():
    variants = pandas.read_csv("~/Desktop/training_variants.txt")
    new_text = pandas.read_csv("~/Desktop/training_text.txt",
                               sep="\\|\\|",
                               engine="python"
    )
    with pandas.option_context('display.max_rows', None, 
                               'display.max_columns', None
                              ):
        print(new_text)
#        print(variants)
    
if __name__=="__main__":
    main()
