#library import
import spacy
from collections import Counter

#Downloading English language model and loding into object
nlp = spacy.load("en_core_web_sm")

#Input text 
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

#Printing the tokens and their index
for token in about_doc:
    print (token, token.idx)

#Performing operation to add stopwords file to object
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

#printing top 10 stop words
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

#Printing the text which do not content STOPWORDS
print([token for token in about_doc if not token.is_stop])

#Lemmatization
#Assigning input text to object
conference_help_doc = nlp(about_text)

#Printing the the root(original) words by removing prefix and suffix
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

#assigning input text to object
complete_doc = nlp(about_text)

#counting the repetate words
words = [
    token.text
    for token in complete_doc
    if not token.is_stop and not token.is_punct
]

#printing number of timing it will occur 
print(Counter(words).most_common(5))

#Part-of-Speech Tagging
#printing the part of speech of tokens
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )