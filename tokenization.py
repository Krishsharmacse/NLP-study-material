import nltk
corpus ="""Hello Welcome , to kisu Bhaiya code of NLP
krish sharma's ,hash function ,As you say to bas.
please make a tea! without sugar."""
#Tokenzation 
# sentence -----> PARAGRAPH


nltk.sent_tokenize
print(nltk.sent_tokenize(corpus))
print("\n")
documents = nltk.sent_tokenize(corpus)
for sentence in documents:
    print(sentence)
print("\n")
#Tokenization Sentence to word
print(nltk.word_tokenize(corpus))

for sentence in documents:
    print(nltk.word_tokenize(sentence))
print("\n")
print(nltk.wordpunct_tokenize(corpus))##punctuation will get seperated
print("\n")
tokenizer=nltk.TreebankWordTokenizer() ##tokenizer made by me
tokenizer.tokenize(corpus)
print("\n")

