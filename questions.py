def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}".format(capitalized)


print("You can always quit with 'quit' ")
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "quit":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
