import pickle
import re


existing_vocab =  pickle.load(open('vocab.pkl','rb'))
#print(existing_vocab)

string_pattern_1 = r'\d'
string_pattern_2 = '^one$'

pattern = re.compile()

# Remove words with numbers from vocabulary
a = existing_vocab.items()
# for word, freq in existing_vocab.items():
#     print(word, freq)
updated_vocab = {word: freq for word, freq in existing_vocab.items()for word, freq in existing_vocab.items() if not pattern.search(str(freq))}

# Save the updated vocabulary
with open('updated_vocabulary.pkl', 'wb') as f:
    pickle.dump(updated_vocab, f)


existing_vocab_2 =  pickle.load(open('updated_vocabulary.pkl','rb'))
print(len(existing_vocab_2))

# for word, freq in existing_vocab_2.items():
#     print(word, freq)
