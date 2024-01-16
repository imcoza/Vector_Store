import numpy as np


class VectorStore:
    def __init__(self):
        self.vector_data = {}
        self.vector_index = {}

    def add_vector(self, vector_id, vector):
        self.vector_data[vector_id] = vector
        self.update_index(vector_id, vector)

    def get_vector(self, vector_id):

        """ Get a vector from the vector store
        returns:
            numpy.ndarray:the vector data  if found else return None"""
        return self.vector_data[vector_id]

    def update_index(self, vector_id, vector):
        """
        Update the indexing structure.
        """
        for existing_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector, existing_vector)/(np.linalg.norm(vector) * np.linalg.norm(existing_vector))
            if existing_id not in self.vector_index:
                self.vector_index[existing_id] = {}
            self.vector_index[existing_id][vector_id] = similarity

    def find_similar_vector(self, query_vector, num_result=5):
        result = []
        for vector_id, vector in self.vector_data.items():
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            result.append((vector_id, similarity))
        result.sort(key=lambda x: x[1], reverse=True)
        return result[:num_result]




