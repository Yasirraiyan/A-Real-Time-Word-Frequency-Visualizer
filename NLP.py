# word_tokenizer_graph_no_punkt.py

from nltk.tokenize import TreebankWordTokenizer
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Input Text
text = "Natural Language Processing is fun and exciting. It helps machines understand human language."

# Step 2: Tokenize Text
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

# Step 3: Count Word Frequency
word_freq = Counter(tokens)

# Step 4: Plot Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(word_freq.keys(), word_freq.values(), color='skyblue')
plt.title('Word Frequency')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()

# Step 5: Save as JPEG
plt.savefig("word_frequency_graph.jpeg", format='jpeg')
plt.show()

# Optional: Print tokens and frequency
print("Tokens:", tokens)
print("Word Frequency:", word_freq)
