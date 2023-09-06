from hf_embeddings import Embeddings

sentences = ["This is an example sentence", "Each sentence is converted"]
embeddings = Embeddings().get_embeddings(sentences)
print(embeddings)