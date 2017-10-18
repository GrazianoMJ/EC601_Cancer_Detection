import sys
import os
import csv
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
#    with open("/home/grazianomj/Desktop/"+"training_text.txt", "r") as file:
#        for line in file:
#            if line == "ID,Text\n":
#                continue
#            else:
#                temp = line.split(r"||")
#                with open("/home/grazianomj/Desktop/training_docs/" +
#                          "text{:04d}".format(int(temp[0])) +
#                          ".txt", "w"
#                ) as target:
#                    target.write(temp[1])
    
if __name__=="__main__":
    main()
