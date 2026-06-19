translations = {
    "hello": "bonjour",
    "how are you": "comment allez-vous",
    "good morning": "bonjour",
    "thank you": "merci",
    "i love python": "j'aime python"
}

text = input("Enter English text: ").lower()

if text in translations:
    print("French Translation:", translations[text])
else:
    print("Translation not found")
