def emoji_convertor(message):
    words = message.split(" ")
    emoji_map = {
        ":)": "😁",
        ":(": "😒",
    }
    output = ""
    for word in words:
        output += emoji_map.get(word, word) + " "
    return output

message = input("> ")
print(emoji_convertor(message))
