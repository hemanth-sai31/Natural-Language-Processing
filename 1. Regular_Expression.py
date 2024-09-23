import re
text1 = input("Enter the Text 1 = ")
text2 = input("Enter the Text 2 = ")
word = input("Enter the WordS = ")
pattern = fr'\b{word}\b'
match1 = re.search(pattern, text1)
if match1:
    print("found the text 1")
else:
    print("not found in text 1")
match2 = re.search(pattern, text2)
if match2:
    print("found the text 2")
else:
    print("not found in text 2")