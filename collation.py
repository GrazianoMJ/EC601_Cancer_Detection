import re
import numpy
import pandas

DIRECT = "/home/grazianomj/Desktop/"
TARGET = DIRECT+"Test/"
VAR_FILES = "variants"
SOL_FILES = "solutions"
TXT_FILES = "text"
FILE_PREFIX = "test_"
TXT_HEADS = ["ID", "Text"]

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
    txt_df = extract_data(TXT_FILES, ".txt")
    
    # Add a classification column to the end of var_df
    var_df["Class"] = 0

    # Go through sol_df and update the class numbers in var_df
    for i, data in sol_df.iterrows():
        class_list = data["class1":].tolist()
        gene_class = class_list.index(1) + 1
        target_row = var_df[var_df["ID"] == data["ID"]].index
        var_df.loc[target_row, ["Class"]] = gene_class

    # Update var_df so that it only contains rows with class designations
    var_df = var_df[var_df["Class"] != 0]

    # Update txt_df so that it only contains rows from var_df. 
    txt_df = txt_df[txt_df["ID"].isin(var_df["ID"])]

    # Update the ID values in var_df & txt_df so they are sequential.
    rows, columns = var_df.shape
    for i in range(rows):
        var_df.iloc[i, 0] = i
        txt_df.iloc[i, 0] = i

    # Place newly created variants and text dataframes into new documents
    var_df.to_csv(TARGET + FILE_PREFIX + VAR_FILES + ".csv", index=False)
    with open(TARGET+FILE_PREFIX+TXT_FILES+".txt", "w") as file:
        file.write(TXT_HEADS[0]+r"||"+TXT_HEADS[1]+"\n")
        for i, data in txt_df.iterrows():
            text2write = (str(txt_df.get_value(i, TXT_HEADS[0])) + 
                          r"||" +
                          txt_df.get_value(i, TXT_HEADS[1]) +
                          "\n"
            )
            file.write(text2write)
    
if __name__=="__main__":
    main()
