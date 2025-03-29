import nltk
import pandas as pd
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer



# Read the data
messages = pd.read_csv(r"C:\Users\SHUBHAM SHARMA\Desktop\programming\python\AI Course Udemy\NATURAL LANGUAGE PROCESSING\Bag of words\SMSSpamCollection (1).txt",
                       sep='\t', names=['label', 'message'])

# Initialize stemmer
stemmer = nltk.PorterStemmer()
limmitizer = nltk.WordNetLemmatizer()
# Initialize corpus list
corpus = []

# Loop through messages
for i in range(0, len(messages)):
    review = re.sub("[^a-zA-Z]", " ", messages["message"][i])
    review.lower()
    words = nltk.word_tokenize(review)
    words = [limmitizer.lemmatize(j) for j in words if not j in set(stopwords.words("english"))]
    noty = " ".join(words)
    corpus.append(noty)

# Print the corpus
print(corpus)

# Use CountVectorizer from sklearn
# cv = CountVectorizer(max_features=2500, binary=True)
# X = cv.fit_transform(corpus).toarray()
cv = CountVectorizer(max_features=500,binary=True,ngram_range=(3,3))
x = cv.fit_transform(corpus).toarray()

# Print the array representation of the Bag of Words model

print(x)
print(x.shape)
print(f"{cv.vocabulary_}")
print("\n")