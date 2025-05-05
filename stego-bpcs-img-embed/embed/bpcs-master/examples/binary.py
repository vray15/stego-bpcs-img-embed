def text_to_binary(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    binary = ''.join(format(ord(c), '08b') for c in text)
    return binary

binary_data = text_to_binary('text to here')
print(binary_data)
