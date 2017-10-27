import numpy
import pandas

DIRECT = "/home/grazianomj/Desktop/"
TARGET = DIRECT+"Test/"
VAR_FILES = "variants"
SOL_FILES = "solutions"
TXT_FILES = "text"
FILE_PREFIX = "test_"

def extract_data(designation, suffix):
    file_name = DIRECT+FILE_PREFIX+designation+suffix
    if suffix == ".csv":
        return pandas.read_csv(file_name)
    else:
        return pandas.read_csv(file_name, header=0, sep="\\|\\|",
                               engine="python"
        )

def main():
    # Place all data from files into DataFrames
    var_df = extract_data(VAR_FILES, ".csv")
    sol_df = extract_data(SOL_FILES, ".csv")
    
    # Add a classification column to the end of var_df
    var_df["Class"] = 0

    # Go through sol_df and update the class numbers in var_df
#    print(sol_df.iloc[1])
#    temp1 = sol_df.iloc[1]["class1":].tolist()
#    print(temp1)
#    temp2 = var_df[var_df["ID"] == sol_df.iloc[1]["ID"]]
#    print(temp2)
#    gene_class = temp1.index(1) + 1
#    print(gene_class)
#    temp3 = temp2.index
#    print(temp3)
#    var_df.loc[temp3, ["Class"]] = gene_class
#    print(var_df[var_df["ID"] == sol_df.iloc[1]["ID"]])
    for i, data in sol_df.iterrows():
        class_list = data["class1":].tolist()
        gene_class = class_list.index(1) + 1
        target_row = var_df[var_df["ID"] == data["ID"]].index
        var_df.loc[target_row, ["Class"]] = gene_class

    # Update var_df so that it only contains rows with class designations
    var_df = var_df[var_df["Class"] != 0]
    
    with pandas.option_context('display.max_rows', None,
                               'display.max_columns', None
                              ):
        print(var_df)

if __name__=="__main__":
    main()
