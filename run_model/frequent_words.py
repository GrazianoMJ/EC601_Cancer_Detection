#this python code is mainly to find the most common 150 words in traing text
import re
import pandas
import nltk
file_name1="/Users/Iris/study/EC601/cancer_detection/training_text.txt"
file_name2="/Users/Iris/study/EC601/cancer_detection/common_words.txt"
m=nltk.data.load(file_name1) 
allWords= nltk.tokenize.word_tokenize(m)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)
mostCommon= allWordDist.most_common(150)
commonWord=""
for i in range(150):
    commonWord=commonWord+" "+mostCommon[i][0]     
print(commonWord)
with open(file_name2, "w") as file:
    file.write(commonWord)        