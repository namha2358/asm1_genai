# app/bigram_model.py
import random                              # for weighted random sampling of the next word
import re                                  # for regex-based tokenization
from collections import Counter, defaultdict  # Counter = frequency counts; defaultdict = auto-creating dicts


class BigramModel:
    def __init__(self, corpus):
        # corpus is a list of strings (as in main.py) join them into one long text
        text = " ".join(corpus)
        # lowercase and pull out word tokens 
        self.words = re.findall(r"\b\w+\b", text.lower())
        # build the bigram probability table once when the model is created
        self.bigram_probs = self._compute_bigram_probs()

    def _compute_bigram_probs(self):
        # pair each word with the word that follows it: (w1, w2)
        bigrams = list(zip(self.words[:-1], self.words[1:]))
        bigram_counts = Counter(bigrams)       # C(w1, w2)
        unigram_counts = Counter(self.words)   # C(w1)

        probs = defaultdict(dict)
        for (w1, w2), count in bigram_counts.items():
            # MLE formula from the notebook: p(w2 | w1) = C(w1, w2) / C(w1)
            probs[w1][w2] = count / unigram_counts[w1]
        return probs

    def generate_text(self, start_word, length=20):
        current = start_word.lower()           # normalize to match lowercase vocabulary
        generated = [current]                  # start the output with the seed word

        for _ in range(length - 1):
            next_words = self.bigram_probs.get(current)
            if not next_words:                
                break
            # sample the next word using the bigram probabilities as weights
            current = random.choices(
                list(next_words.keys()), weights=list(next_words.values())
            )[0]
            generated.append(current)

        return " ".join(generated)