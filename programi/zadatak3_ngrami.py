"""Zadatak 3 (P5, V5): bigramski model, MLE, Laplace i perpleksija."""
import math
from collections import Counter

corpus = ["ja sam Ana", "Ana ja sam", "ja ne volim zelena jaja i šunku"]

unigrams, bigrams = Counter(), Counter()
for sentence in corpus:
    words = ["<s>"] + sentence.split() + ["</s>"]
    unigrams.update(words)
    bigrams.update(zip(words, words[1:]))

def p_mle(word, prev):
    return bigrams[(prev, word)] / unigrams[prev]

print("P(sam | ja)  =", round(p_mle("sam", "ja"), 3))
print("P(Ana | <s>) =", round(p_mle("Ana", "<s>"), 3))

V = len(unigrams)                     # veličina rječnika (s <s> i </s>)

def p_laplace(word, prev):
    return (bigrams[(prev, word)] + 1) / (unigrams[prev] + V)

def perplexity(sentence, p):
    words = ["<s>"] + sentence.split() + ["</s>"]
    log_prob = 0
    for prev, word in zip(words, words[1:]):
        prob = p(word, prev)
        if prob == 0:
            return math.inf           # neviđeni bigram: vjerojatnost 0
        log_prob += math.log(prob)    # zbrajamo logaritme (nema potkoračenja)
    n = len(words) - 1                # broj predviđanja (riječi + </s>)
    return math.exp(-log_prob / n)

test = "Ana sam ja"
print("V =", V)
print("MLE:    ", perplexity(test, p_mle))
print("Laplace:", round(perplexity(test, p_laplace), 2))

# samoprovjera
assert round(p_mle("sam", "ja"), 3) == 0.667 and round(p_mle("Ana", "<s>"), 3) == 0.333
assert V == 11 and perplexity(test, p_mle) == math.inf
assert round(perplexity(test, p_laplace), 2) == 11.34
