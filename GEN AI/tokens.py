import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sample_text = 'Eu amo programação'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)