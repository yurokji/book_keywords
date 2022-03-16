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
# newStopWords = ["jews","people", "br", "href", "jew", "could", "would", "even", "germany", "since", "one", "eichmanns", "thing",  "upon", "something", "therefore", "can", "say", "tell", "cannot", "able", "things", "gutenberg", "http",
# "www", "httpwwwidphnet", "IDPH", "may", "also", "Ye", "Henricks", "Te", "Lao", "Tzu", "Ching", "Te Ching", "taoist", "chapter", "translation", "version", "chapters", "translations", "English", "interpretation"]

# stopwords.extend(newStopWords)
# wc = WordCloud(width=1000, height=600, background_color="white", random_state=0)






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

