# app/embeddings.py
import spacy


class EmbeddingModel:
    def __init__(self, model_name="en_core_web_lg"):
        # Load the spaCy model ONCE when the server starts.
        # Loading is slow (~1-2 sec), so we never want to do it per request.
        self.nlp = spacy.load(model_name)

    def get_embedding(self, text):
        # Run the text through spaCy; .vector gives the embedding
        # (for a single word: its word vector; for a sentence: the average of word vectors)
        doc = self.nlp(text)
        # .tolist() converts the numpy array into a plain Python list so FastAPI can turn it into JSON
        return doc.vector.tolist()

    def has_vector(self, text):
        # True if spaCy actually knows this text (unknown words get an all-zero vector)
        return self.nlp(text).has_vector

    def get_similarity(self, text1, text2):
        # Cosine similarity between two texts (same idea as calculate_similarity in Module 2)
        return float(self.nlp(text1).similarity(self.nlp(text2)))