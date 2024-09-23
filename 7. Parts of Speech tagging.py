import nltk
nltk.download('punkt')

def pos_tagging(text):

    words = nltk.word_tokenize(text)

    pos_tags = nltk.pos_tag(words)
    return pos_tags

text = "Good Morning students"
text1="Pay attention please"
text2="He is the founder of our university"
tags = pos_tagging(text)
print(tags)
tagss = pos_tagging(text1)
print(tagss)
tagsss = pos_tagging(text2)
print(tagsss)
