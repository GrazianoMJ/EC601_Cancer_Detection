import re
import pandas
from nltk import word_tokenize
from nltk.corpus import stopwords

DIRECT = "/home/grazianomj/Desktop/"
TARGET = ["Training/", "Test/"]
FILE_PREFIX = ["training_", "test_"]
TXT_HEADS = ["ID", "Text"]
STOPS = set(stopwords.words("english"))

def simple_text(raw_text):
    no_syms = re.sub("[\W]", " ", raw_text)
    tokens = word_tokenize(no_syms)
    no_stops = [w for w in tokens if not w in stopwords.words("english")]
    clean_text = " ".join(no_stops)
    return clean_text

def extract_data(folder, prefix, designation, suffix):
    file_name = DIRECT+folder+prefix+designation+suffix
    if suffix == ".csv":
        return pandas.read_csv(file_name)
    else:
        return pandas.read_csv(file_name, header=0, sep="\\|\\|",
                               engine="python"
        )

def main():
    for i in range(1,2):
        file_name1 = DIRECT+TARGET[i]+FILE_PREFIX[i]+"text.txt"
        file_name2 = DIRECT+TARGET[i]+FILE_PREFIX[i]+"_mod_text.txt"
        txt_df = pandas.read_csv(file_name1, header=0, sep="\\|\\|",
                                 engine="python"
        )
    
        text_size = txt_df[TXT_HEADS[1]].size
        clean_text_docs = []
        for row in range(0, text_size):
            if (row+1)%50 == 0 or not row:
                print("Review {} of {} in progress".format(row+1, text_size))
            clean_text_docs.append(simple_text(txt_df.get_value(row, TXT_HEADS[1])))
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
