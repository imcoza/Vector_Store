 **README.md**

# Sentence Similarity Search Using VectorStore

**This project demonstrates how to use the VectorStore class to efficiently find similar sentences based on their semantic content.**

## Files

- **main.py:** Contains the VectorStore class definition (see separate README for details).
- **app.py:** Demonstrates how to use the VectorStore class for sentence similarity search.

## Running the Example

1. **Prerequisites:**
- Python 3.6 or later
- NumPy

   ```bash
   pip install numpy
   ```

3. **Run the example:**

   ```bash
   python main.py
   ```

## Example Output

```
Query sentence:  Mango is the best fruit.
Similar sentences:
mango is my favourite fruit.: Similarity = 0.8165
I eat mangoes.: Similarity = 0.7071
```

## Key Concepts

1. **VectorStore Class:** Provides efficient storage and retrieval of vectors, optimized for similarity search.
2. **Text Vectorization:** Converts sentences into numerical vectors representing their semantic content.
3. **Cosine Similarity:** Measures the similarity between vectors, used to find similar sentences.

## Steps in the Example Code

1. **Imports:** Imports the VectorStore class and NumPy.
2. **Creates VectorStore:** Initializes a VectorStore instance.
3. **Defines Sentences:** Creates a list of sample sentences.
4. **Tokenization:** Splits sentences into tokens (words).
5. **Creates Vocabulary:** Builds a set of unique words from the sentences.
6. **Word-to-Index Mapping:** Assigns unique numerical indices to words in the vocabulary.
7. **Vectorization:** Converts sentences into numerical vectors using the word-to-index mapping and counts of words.
8. **Adds Vectors to Store:** Adds the sentence vectors to the VectorStore.
9. **Query Sentence:** Defines a query sentence to search for similar sentences.
10. **Vectorizes Query:** Converts the query sentence into a vector using the same method as for the original sentences.
11. **Finds Similar Sentences:** Uses the VectorStore's `find_similar_vector` method to retrieve similar sentences based on cosine similarity.
12. **Prints Results:** Prints the query sentence and the retrieved similar sentences along with their similarity scores.
