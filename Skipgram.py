from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
import nltk
corpous = "The quick brown fox jumps over the lazy dog, but the sly cat stays hidden behind the bushes."
tokenizesentence = nltk.sent_tokenize(corpous)
lemetaizer = WordNetLemmatizer().lemmatize
stopword = stopwords.words('english')
processedsentence=[]

for i in range(len(tokenizesentence)):
    tokenizeword = word_tokenize(tokenizesentence[i])
    processsword = [lemetaizer(word) for word in tokenizeword if not word in set(stopword)]
    processedsentence.append(processsword)
skipgrammodel = Word2Vec(sentences = processedsentence,vector_size=100,window = 5,min_count=1,sg=1)
skipgramvector = skipgrammodel.wv['sly']
print(skipgramvector)

skipgrammodel.save("skipgram.model")