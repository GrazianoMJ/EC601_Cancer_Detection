#this python code is mainly to find the most common 500 words in traing text
import re
import pandas
import nltk

file_name1="/Users/Iris/study/EC601/cancer_detection/training_text.txt"
file_name2="/Users/Iris/study/EC601/cancer_detection/common_words_origin.txt"
m=nltk.data.load(file_name1) 
allWords= nltk.tokenize.word_tokenize(m)
mostCommon= allWordDist.most_common(500)
commonWord=""
for i in range(500):
    commonWord=commonWord+" "+mostCommon[i][0]
    
with open(file_name2, "w") as file:
    file.write(commonWord)      
#print(commonWord)
