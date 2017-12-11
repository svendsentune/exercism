import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    return all([l in sentence.lower() for l in alphabet])
