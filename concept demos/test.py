import openai
from openai.embeddings_utils import get_embedding
import numpy as np

# Set up OpenAI API credentials
openai.api_key = "OPENAI API KEY"

# Define the text to encode as a vector
text = "Enter your text here."

# Define the model to use for encoding
model = "text-davinci-002"

# Encode the text using the specified model
response = openai.Completion.create(
    engine=model,
    prompt=text,
    max_tokens=1,
    n=1,
    stop=None,
    temperature=0,
    return_prompt=False,
    return_sequences=False,
    return_metadata=False,
    logprobs=None,
)

# Extract the encoded vector from the response
vector = np.array(response.choices[0].embedding)

print("Encoded vector:")
print(vector)

