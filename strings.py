""""
This module practice working with string data type
"""

message = 'Hello, World!'
some_text = "Bobby's World"
multiline_text = """Bobby's World is the name of animation
at the end of 1990's."""

replaced_message = message.replace('World', 'Universe')

print(message)
print(type(message))
print(len(message))

# Some methods of str object
print(message.lower())
print(message.upper())
print(message.capitalize())
print(message.count('He'))
print(message.count('l'))
print(message.count('universe'))
print(message.find('World'))
print(replaced_message)

# Indexing
print(message[0])
print(message[12])
print(message[-1])

# Slicing
print(message[:4])
print(message[6:])
print(message[::-1])

# Show all methods of an object
print(dir(message))

# Show Documentation Help of anything
# print(help(str))
print(help(str.translate))


print(some_text)
print(multiline_text)
