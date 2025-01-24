#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    start = 0

    while start < len(text):
        if text[start] in characters:
            print(text[start])
            print()
            start += 1
            while start < len(text) and text[start] == " ":
                start += 1
        else:
            print(text[start], end="")
            start += 1
