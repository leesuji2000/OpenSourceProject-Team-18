from openai import OpenAI
import numpy as np
from dotenv import load_dotenv
import os


load_dotenv()  # take environment variables from .env.
gpt_key = os.getenv('GPT_KEY')
# Initialize the OpenAI client with the API key
client = OpenAI(api_key=gpt_key)

def get_embedding(text, model="text-embedding-3-small"):
    """
    Fetches the embedding for a given text using the specified model.
    
    Args:
    text (str): The text for which to compute the embedding.
    model (str): The model to use for computing the embedding.

    Returns:
    np.ndarray: The computed embedding as a numpy array.
    """
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    embedding = response.data[0].embedding
    return np.array(embedding)

def find_most_similar_word(input_text, embeddings):
    """
    Finds the word that has the most similar embedding to the given input text.

    Args:
    input_text (str): The input text to compare against the embeddings.
    embeddings (dict): A dictionary of word to embeddings.

    Returns:
    str: The word that is most similar to the input text.
    """
    input_embedding = get_embedding(input_text)
    max_similarity = -1
    most_similar_word = None
    
    # Calculate cosine similarity with each word in the embeddings dictionary
    for word, embedding in embeddings.items():
        similarity = np.dot(input_embedding, embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(embedding))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_word = word

    return most_similar_word

# List of words to compute embeddings for
words = ["사랑", "고구마", "음식", "자동차", "핸드폰", "보트", "바나나", "충전기", "슬픔", "책", "컴퓨터", "노트북"]

# Precompute embeddings for the given list of words
embeddings = {word: get_embedding(word) for word in words}

# Example usage: Find the most similar word to "휴대폰"
input_word = "기쁘다"
most_similar = find_most_similar_word(input_word, embeddings)

# Uncomment the line below to print the result in a live environment
print("가장 유사한 단어:", most_similar)
# Compute the embedding for the word "사랑"
embedding_love = get_embedding("사랑")
print("임베딩 값:", embedding_love)