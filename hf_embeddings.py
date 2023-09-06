from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

class Embeddings:
    def __init__(self, model = 'sentence-transformers/all-mpnet-base-v2' ) -> None:
        self.model = SentenceTransformer(model)
    
    def get_embeddings(self, text):
        return self.model.encode(text)
    
