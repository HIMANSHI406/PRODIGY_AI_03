import random

# Read input corpus
with open("input_corpus.txt", "r") as file:
    text = file.read()

# Create a list of words
words = text.split()

# Create a dictionary to hold the Markov chain
markov_chain = {}

# Build the chain using pairs of words
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

# Generate new text
def generate_text(chain, length=50):
    current_word = random.choice(list(chain.keys()))
    result = [current_word]

    for _ in range(length - 1):
        next_words = chain.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)

    return " ".join(result)

# Generate and print text
generated_text = generate_text(markov_chain, length=50)
print("Generated Text:\n")
print(generated_text)
