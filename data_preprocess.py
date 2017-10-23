import re
import pandas
from nltk import word_tokenize
from nltk.corpus import stopwords

DIRECT = "/home/grazianomj/Desktop/"
VAR_HEADS = ["ID", "Gene", "Variation", "Class"]
TXT_HEADS = ["ID", "Text"]
STOPS = set(stopwords.words("english"))

def simple_text(raw_text):
    no_syms = re.sub("[\W]", " ", raw_text)
    tokens = word_tokenize(no_syms)
    no_stops = [w for w in tokens if not w in stopwords.words("english")]
    clean_text = " ".join(no_stops)
    return clean_text

def main():
    variants = pandas.read_csv(DIRECT+"training_variants.txt")
    text = pandas.read_csv(DIRECT+"training_text.txt",
                               header=0,
                               sep="\\|\\|",
                               engine="python"
    )

    text_size = text[TXT_HEADS[1]].size
    clean_text_docs = []
    for row in range(0, text_size):
        if (row+1)%50 == 0 or not row:
            print("Review {} of {} in progress".format(row+1, text_size))
        clean_text_docs.append(simple_text(text.get_value(row, TXT_HEADS[1])))
    with open(DIRECT+"training_text_mod.txt", "w") as file:
        file.write(TXT_HEADS[0]+r"||"+TXT_HEADS[1]+"\n")
        for row in range(0, text_size):
            text2write = (str(text.get_value(row,TXT_HEADS[0])) + 
                          r"||" +
                          clean_text_docs[row] +
                          "\n"
            )
            file.write(text2write)

if __name__=="__main__":
    main()
