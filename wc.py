import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from statistics import mean
from wordcloud import WordCloud
import regex
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()

# filename = "tao"
# filename = "world as will"
# filename = "phenomenon of spirit"
# filename = "tractatus"
# filename = "Popper"
# filename = "prince"
# filename = "emile"
# filename = "capital one"
# filename = "being and time"
# filename = "morals"
# filename = "eichmann"
# filename = "sickness"
filename = "pure reason"
# filename = "nichomachean"
# filename = "proust_all"


f=open("./txts/" + filename + ".txt",'r')
lines = f.readlines()
f.close()

text = ""
for line in lines:
    l =""
    for word in line:
        w = lm.lemmatize(word)
        w.lower()
        l += w
    text += l


# print(text)


stopwords = nltk.corpus.stopwords.words("english")
stopwords = list(set(stopwords))
newStopWords = ["jews","people", "br", "href", "jew", "may", "might", "should", "have", "has", "had", "make", "making", "made", "get", "getting", "gotten", "become", "became", "can", "can\'t", "cannot", "did", "do", "dont", "don\'t", "does", "doesn\'t",  "done", "haven\'t", "could", "couldn\'t", "would", "wouldn\'t", "even", "germany", "since", "one", "eichmanns", "thing",  "upon", "something", "therefore", "thus", "otherwise", "consequently", "long", "short", "people", "man", "men", "person", "while", "can", "say", "tell", "cannot", "able", "things", "gutenberg", "http", "page", "www", "httpwwwidphnet", "IDPH", "may", "also", "Ye", "Section", "chapter", "translation", "version", "chapters", "translations", "English", "interpretation"]

stopwords.extend(newStopWords)
wordcloud = WordCloud(width=2560, height=1440, background_color="black", random_state=0, \
    max_words=150, stopwords=stopwords).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("./images/" + filename + '_eng_.png', dpi=1200)
plt.show()


import googletrans 
translator = googletrans.Translator() 

import copy
# mydic=copy.deepcopy(wordcloud.words_)
mydic = {}
for eng_key in wordcloud.words_.keys():
    trans_key = translator.translate(eng_key, dest='ko') 
    mydic[trans_key.text] = wordcloud.words_[eng_key]



# print(mydic)
wc = WordCloud(font_path="./NanumGothic.ttf", background_color="black",random_state=0, width=2560,height=1440, max_words=150).generate_from_frequencies(mydic)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig("./images/" + filename + '_kor_.png', dpi=1200)
plt.show()

