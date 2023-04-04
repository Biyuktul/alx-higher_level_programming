#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    buffer = ''
    for i in text:
        if i in chars:
            buffer += i + "\n\n"
            # text_indentation('.?:')
        else:
            buffer += i

    lines = buffer.split('\n')
    print(lines)
    for line in lines:
        print(line.strip())
