import re
import pandas
import nltk


DIRECT = "/Users/Iris/study/EC601/cancer_detection/"
FILE_PREFIX = ["training_", "test_"]
TXT_HEADS = ["ID", "Text"]
STOPS = set(nltk.corpus.stopwords.words("english"))
#nltk.corpus.stopwords.words("english")&&


def simple_text(raw_text,common):
    no_syms = re.sub("[\W]", " ", raw_text)
    tokens = nltk.tokenize.word_tokenize(no_syms)
    no_stops = [w for w in tokens if not w in common]
    clean_text = " ".join(no_stops)
    return clean_text

def main():
    for i in range(1):
        file_name1 = DIRECT+FILE_PREFIX[i]+"text.txt"
        file_name2 = DIRECT+FILE_PREFIX[i]+"_frequent2_text.txt"
        file_name3 = DIRECT+"common_words.txt"
        txt_df = pandas.read_csv(file_name1, header=0, sep="\\|\\|",
                                 engine="python"
        )
        text_size = txt_df.shape[0]
        print(txt_df.shape)
        clean_text_docs = []

#==============================================================================

#        commonWord=" , the . of ) ( and in to a with that for were mutations is by was as cells ; or are we this from % at these cell on not et 1 mutation fig be figure cancer an patients have 2 protein which activity expression [ ] : al. mutant also variants been using domain tumor all kinase data gene 3 analysis brca1 mutants tumors other table may dna activation it two binding wild-type our has egfr but results 5 4 shown both between genes than proteins one used identified human exon found 10 growth study more had can no clinical signaling p53 levels only lines after each functional observed however al its kit studies b assay most different function such three residues supplementary their treatment phosphorylation cases pten > into reported associated previously resistance number 6 control showed c samples assays response compared sequence = pathway described"
        with open(file_name3,"r") as file:
            commonWord=file.readlines()
        for row in range(text_size):   
            if (row+1)%50 == 0 or not row:
                print("Review {} of {} in progress".format(row+1, text_size))
            clean_text_docs.append(simple_text(txt_df.get_value(row,0,takeable=True),commonWord))
        with open(file_name2, "w") as file:
            for row in range(text_size):
                file.write(str(row)+r"||")
                text2write =clean_text_docs[row] +"\n"
                file.write(text2write)
 

#==============================================================================
# [(',', 1764670), ('the', 1516717), ('.', 1381284), ('of', 1241947), (')', 938373), 
# ('(', 938017), ('and', 929893), ('in', 913517), ('to', 566479), ('a', 462152), 
# ('with', 390168), ('that', 291288), ('for', 276852), ('were', 261748),
#  ('mutations', 236702), ('is', 215039), ('by', 213826), ('was', 213233),
#  ('as', 195096), ('cells', 183678), (';', 163795), ('or', 159458), ('are', 147446),
#  ('we', 140837), ('this', 132680), ('from', 129648), ('%', 128309), ('at', 118480), 
#  ('these', 114905), ('cell', 113663), ('on', 113458), ('not', 108429), ('et', 104568),
#  ('1', 102455), ('mutation', 102341), ('fig', 100217), ('be', 98195), ('figure', 97087),
#  ('cancer', 91102), ('an', 90983)]
#==============================================================================
#            
if __name__=="__main__":
    main()