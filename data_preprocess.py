import sys
import os
import pandas

def main():
    variants = pandas.read_csv("~/Desktop/training_variants.txt")
#    with pandas.option_context('display.max_rows', None, 
#                               'display.max_columns', None
#                              ):
#        print(variants)
    with open("/home/grazianomj/Desktop/"+"training_text.txt", "r") as file:
        for line in file:
            if line == "ID,Text\n":
                continue
            else:
                temp = line.split(r"||")
                with open("/home/grazianomj/Desktop/training_docs/" +
                          "text{:04d}".format(int(temp[0])) +
                          ".txt", "w"
                ) as target:
                    target.write(temp[1])
    
if __name__=="__main__":
    main()
