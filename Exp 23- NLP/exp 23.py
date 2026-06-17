text = "Ram plays cricket. He likes sports."

sentences = text.split(".")

if len(sentences) > 1:
    print("Text is coherent")
else:
    print("Text is not coherent")
