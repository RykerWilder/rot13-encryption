import string

def rot13(text):
    rot13_trans = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13] + 
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    )
    return text.translate(rot13_trans)