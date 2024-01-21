 **README.md**

# Implementing a VectorStore for Cosine Similarity-based Semantic Retrieval

**This project demonstrates how to build the custom-based VectorStore class implemented from scratch to find similar sentences.**

![Vector Store](https://python.langchain.com/assets/images/vector_stores-125d1675d58cfb46ce9054c9019fea72.jpg)

# Aim of the Project

**The project aims to implement a VectorStore class that can be used to effectively find similar sentences based on the Cosine Similarity Score. This involves implementing techniques for representing sentences as vectors, indexing those vectors in the custom VectorStore, and efficiently searching for similar vectors based on their meaning.**

## Files in the project:

- **main.py:** Contains the VectorStore class definition. 
- **app.py:** Demonstrates using the VectorStore class for sentence similarity search.
 
## Example Output

```
Query sentence:  Mango is the best fruit.
Similar sentences:
mango is my favorite fruit.: Similarity = 0.8165
I eat mangoes.: Similarity = 0.7071
```

## Key Concepts

1. **VectorStore Class:** Provides efficient storage and retrieval of vectors, optimized for similarity search.
2. **Text Vectorization:** Converts sentences into numerical vectors representing their semantic content.
3. **Cosine Similarity:** Measures the similarity between vectors. 
