import re
import pandas
import nltk
counts = dict()
file_name1="/Users/Iris/study/EC601/cancer_detection/training_text.txt"
file_name2="/Users/Iris/study/EC601/cancer_detection/rare_words_3.txt"
txt_df = pandas.read_csv(file_name1, encoding='UTF-8' ,header=0, sep="\\|\\|",
                                 engine="python"
        )
text_size = txt_df.shape[0]
for row in range(text_size):   
            if (row+1)%50 == 0 or not row:
                print("Review {} of {} in progress".format(row+1, text_size))
            no_syms = re.sub("[\W]", " ", txt_df.get_value(row,0,takeable=True))
            tokens = nltk.tokenize.word_tokenize(no_syms)
            for word in tokens:
                if word in counts.keys():
                    counts[word] += 1
                else:
                    counts[word] = 1
l=[key for (key, value) in counts.items() if value in [1,2,3]]
rareword = ""
for w in l:
    rareword += w+" "
    
with open(file_name2, "w",encoding='UTF-8') as f2:
    f2.write(rareword)