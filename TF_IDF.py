import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import numpy
from sklearn.feature_extraction.text import CountVectorizer
import pandas
paragraph = pandas.read_csv(r"C:\Users\SHUBHAM SHARMA\Desktop\programming\python\AI Course Udemy\NATURAL LANGUAGE PROCESSING\words into vectors\SMSSpamCollection (1).txt",
                            sep='\t', names=['label', 'message'])
lemmitizer = WordNetLemmatizer()
corpus =[]
for i in range(0,len(paragraph)):
    review = re.sub("[^a-zA-Z]"," ",paragraph["message"][i])
    review = review.lower()
 
    words = nltk.word_tokenize(review)
    words = [lemmitizer.lemmatize(j) for j in words if not j in set(stopwords.words("english"))]
    sentence = " ".join(words)
    corpus.append(sentence)
# x = CountVectorizer(max_features=250,binary=True,ngram_range=(2,2))
# y = x.fit_transform(corpus).toarray()
x = TfidfVectorizer(max_features=200,ngram_range=(1,1))
y=x.fit_transform(corpus).toarray()
numpy.set_printoptions(edgeitems=30,linewidth=10000)
formatter=dict(float=lambda y: "%.3g" % y)

print(y)