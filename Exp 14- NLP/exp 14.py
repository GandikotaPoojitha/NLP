sentence = "He runs"

words = sentence.split()

if words[0] == "He" and words[1].endswith("s"):
    print("Sentence has correct agreement")
else:
    print("Agreement error")
