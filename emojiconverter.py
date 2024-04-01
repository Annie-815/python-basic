message = input("message: ")
words = message.split(" ")
emoji_converter = {
    ":)": "😂",
    ":(": "😔"
}
output = " "
for word in words:
    output += emoji_converter.get(word, word) + " "
print(output)