test_words = ["cat", "dog", "bus", "box", "baby", "child", "person"]
for word in test_words:
    if word == "child":
        plural = "children"
    elif word == "person":
        plural = "people"
    elif word.endswith("y") and word[-2] not in "aeiou":
        plural = word[:-1] + "ies"
    elif word.endswith(("s", "sh", "ch", "x", "z")):
        plural = word + "es"
    else:
        plural = word + "s"

    print(f"Plural of '{word}' is '{plural}'")