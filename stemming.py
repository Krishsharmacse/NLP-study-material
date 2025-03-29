import nltk
#Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma.
#  Stemming is important in natural language understanding (NLU) and natural language processing (NLP).
## Classification Problem
## Comments of product is a positive review or negative review
## Reviews----> eating, eat,eaten [going,gone,goes]--->go

##word = ['Hello', 'Welcome', ',', 'to', 'kisu', 'Bhaiya', 'code', 'of', 'NLP', 'krish', 'sharma', "'", 's', ',', 'hash', 'function', ',', 'As', 'you', 'say', 'to', 'bas', '.', 'please', 'make', 'a', 'tea', '!', 'without', 'sugar', '.']
#### PorterStemmer
word=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]
steming = nltk.PorterStemmer()
for words in word:
    print(words+"---->"+steming.stem(words))
print('\n')
print(steming.stem("kisu gaming"))
print('\n')
print(steming.stem("split"))
##### RegexpStemmer class
##NLTK has RegexpStemmer class with the help of which we can easily implement Regular Expression Stemmer algorithms. 
# It basically takes a single regular expression and removes any prefix or suffix that matches the expression. Let us see an example
print("regular stemmer")
Regstem =nltk.RegexpStemmer('ing$|s$|e$|able$')
for i in word:
    print(i+ "-------->"+Regstem.stem(i))
print(Regstem.stem("congratulatiions"))
print(Regstem.stem("eating"))
print("\n")
##### Snowball Stemmer
## It is a stemming algorithm which is also known as the Porter2 stemming algorithm as 
# it is a better version of the Porter Stemmer since some issues of it were fixed in this stemmer.
snow_stemming = nltk.SnowballStemmer("english")
for i  in word:
    print(i+"------------->"+snow_stemming.stem(i))
print(snow_stemming.stem("fairly"))
print(steming.stem("fairly"))