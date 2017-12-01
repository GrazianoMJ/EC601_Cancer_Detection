""" data_preprocess.py
    Author: Mike Graziano
    This code is designed to go through both the Training & Test text
    provided to the team from Kaggle and performs preprocessing tasks.
    These tasks include:
    1.) Remove common words that add no value (provided by the 
        nltk.corpus.stopwords commands)
    2.) Remove all symbols to look only at the text.
"""    

import re
import pandas
from nltk import word_tokenize
from nltk.corpus import stopwords

DIRECT = "/home/grazianomj/Desktop/"
TARGET = ["Training/", "Test/"]
FILE_PREFIX = ["training_", "test_"]
TXT_HEADS = ["ID", "Text"]

# Stopwords contains a list of english words such as "am", "with",
# "and", etc. that are very common but add no value to understanding a
# documents contents.
STOPS = set(stopwords.words("english"))


def simple_text(raw_text):

    """ Simplifies the raw_text by:
        1.) Using regular expressions to remove symbols
        2.) Breaking the words into tokens (a list of strings)
        3.) Removing stopwords from the list of strings
        4.) Reconstructing the text using the join command.
    """

    no_syms = re.sub("[\W]", " ", raw_text)
    tokens = word_tokenize(no_syms)
    no_stops = [w for w in tokens if not w in stopwords.words("english")]
    clean_text = " ".join(no_stops)
    return clean_text


def extract_data(folder, prefix, designation, suffix):
    
    """ extract_data: Accesses the target text file in the computer's
        file system and imports the data into a pandas Dataframe using
        the "read_csv" command.
    """

    file_name = DIRECT+folder+prefix+designation+suffix
    if suffix == ".csv":
        return pandas.read_csv(file_name)
    else:
        return pandas.read_csv(file_name, header=0, sep="\\|\\|",
                               engine="python"
        )

def main():

    """ Main function of the program:
        1.) Goes through both the training and target text using a for
            loop.
        2.) Performs the text cleaning by iterating through the pandas
            Dataframe created.
        3.) Recreates the text file so due to the long nature of the
            preprocess. This will allow for faster training programming
    """

    # Goes through training and text files (only two iterations)
    for i in range(0,2):
        file_name1 = DIRECT+TARGET[i]+FILE_PREFIX[i]+"text.txt"
        file_name2 = DIRECT+TARGET[i]+FILE_PREFIX[i]+"_mod_text.txt"
        txt_df = pandas.read_csv(file_name1, header=0, sep="\\|\\|",
                                 engine="python"
        )
        text_size = txt_df[TXT_HEADS[1]].size

        # Calls simple_text for each string AND adds them to a new list
        # Also prints out progress
        clean_text_docs = []
        for row in range(0, text_size):
            if (row+1)%50 == 0 or not row:
                print("Review {} of {} in progress".format(row+1, text_size))
            clean_text_docs.append(simple_text(txt_df.get_value(row, TXT_HEADS[1])))

        # Opens a new file to save the updated text strings.
        with open(file_name2, "w") as file:
            file.write(TXT_HEADS[0]+r"||"+TXT_HEADS[1]+"\n")
            for row in range(0, text_size):
                text2write = (str(txt_df.get_value(row,TXT_HEADS[0])) + 
                              r"||" +
                              clean_text_docs[row] +
                              "\n"
                )
                file.write(text2write)

if __name__=="__main__":
    main()
