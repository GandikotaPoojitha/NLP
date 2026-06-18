
def generate_text(prompt):
    
    responses = {
        "Artificial Intelligence":
        "Artificial Intelligence is transforming the world by enabling smart machines and automation.",

        "Python":
        "Python is a powerful programming language used in web development, AI, and data science.",

        "Machine Learning":
        "Machine Learning helps computers learn patterns from data and make predictions."
    }

    for key in responses:
        if key.lower() in prompt.lower():
            return responses[key]

    return prompt + " is an important topic in modern technology."


prompt = input("Enter a prompt: ")

output = generate_text(prompt)

print("\nGenerated Text:")
print(output)
