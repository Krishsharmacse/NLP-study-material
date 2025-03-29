import nltk
## Wordnet Lemmatizer
#Lemmatization technique is like stemming. The output we will get after lemmatization is called ‘lemma’,
#  which is a root word rather than root stem, the output of stemming. 
# After lemmatization, we will be getting a valid word that means the same thing.

#NLTK provides WordNetLemmatizer class which is a thin wrapper around the wordnet corpus.
#  This class uses morphy() function to the WordNet CorpusReader class to find a lemma. Let us understand it with an example −
lemmatizer=nltk.WordNetLemmatizer()
'''
POS- Noun-n
verb-v
adjective-a
adverb-r
'''
word=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]
print(lemmatizer.lemmatize("going",pos="v"))
print("\n")
for i in word:
    print(i +"--------->"+ lemmatizer.lemmatize(i,pos="v"))
print(lemmatizer.lemmatize("goes"))
print(lemmatizer.lemmatize("fairly"))