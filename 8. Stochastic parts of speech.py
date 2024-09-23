corpus = [
    (["the", "cat", "sat"], ["DET", "NOUN", "VERB"]),
    (["the", "dog", "barked"], ["DET", "NOUN", "VERB"]),
    (["a", "cat", "meowed"], ["DET", "NOUN", "VERB"]),
    (["the", "dog", "ran"], ["DET", "NOUN", "VERB"])
]
word_tag_probs = {}
for sentence, tags in corpus:
    for word, tag in zip(sentence, tags):
        if word not in word_tag_probs:
            word_tag_probs[word] = {}
        if tag not in word_tag_probs[word]:
            word_tag_probs[word][tag] = 0
        word_tag_probs[word][tag] += 1
for word in word_tag_probs:
    total = sum(word_tag_probs[word].values())
    for tag in word_tag_probs[word]:
        word_tag_probs[word][tag] /= total
def simple_pos_tag(sentence):
    tags = []
    for word in sentence:
        if word in word_tag_probs:
            tag = max(word_tag_probs[word], key=word_tag_probs[word].get)
        else:
            tag = "NOUN" 
        tags.append(tag)
    return tags

new_sentence = ["the", "cat", "ran"]
tags = simple_pos_tag(new_sentence)
print(list(zip(new_sentence, tags)))