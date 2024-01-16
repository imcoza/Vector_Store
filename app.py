from main import VectorStore
import numpy as np

vector_store = VectorStore()
sentences = [
    "I eat mangoes.",
    "mango is my favourite fruit.",
    "mango,apple and orange are fruits.",
    "fruits are good for health."
    ]
# Tokenization
vocabulary = set()
for sentence in sentences:
    tokens = sentence.lower().split()
    vocabulary.update(tokens)
# Assign unique indices to words in vocab
word_to_index = {word: i for i, word in enumerate(vocabulary)}
# Vectorization
sentence_vectors = {}
for sentence in sentences:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocabulary))
    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[sentence] = vector
# Adding vector in vector store
for sentence, vector in sentence_vectors.items():
    vector_store.add_vector(sentence, vector)
# Searching for similarity
query_sentence = "Mango is the best fruit."
query_vector = np.zeros(len(vocabulary))
query_tokens = query_sentence.lower().split()
for token in query_tokens:
    if token in word_to_index:
        query_vector[word_to_index[token]] += 1
similar_sentences = vector_store.find_similar_vector(query_vector, num_result=2)
print("Query sentence: ", query_sentence)
print("Similar sentences: ")
for sentence, similarity in similar_sentences:
    print(f"{sentence}: Similarity = {similarity : .4f}")
